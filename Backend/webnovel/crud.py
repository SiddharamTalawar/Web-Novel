from models import Novel, Chapter, SessionDep, Bookmark,User, Rating, NovelView,NovelRank,Genre
from sqlalchemy.orm import Session
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
import schemas as schemas
from schemas import Novel_schema, Chapter_schema, genre_schema,genre_schema_out,user_schema,bookmark_schema,rating_schema,NovelView_schema
import random


def get_novels(session: SessionDep) -> list[Novel]:
    novels = session.exec(select(Novel)).all()
    return novels


def get_chapters(session: SessionDep, novel_id: int) -> list[Chapter]:
    chapters = session.exec(select(Chapter).where(Chapter.novel_id == novel_id)).all()
    return chapters


def get_novel(session: SessionDep, novel_id: int) -> Novel:
    novel = session.get(Novel, novel_id)
    return novel


def get_chapter(session: SessionDep, chapter_id: int) -> Chapter:
    chapter = session.get(Chapter, chapter_id)
    chapter.read = True       #todo: check weather the chapter is read works after creating /changing database
    return chapter



def create_novel(session: SessionDep, novel: Novel_schema) -> Novel:
    novel = Novel(title=novel.title, description=novel.description, author=novel.author)
    session.add(novel)
    session.commit()
    session.refresh(novel)
    return novel

def update_novel(session: SessionDep, novel_id: int, novel: schemas.Novel_schema) -> schemas.Novel_schema:
    novel_db = session.exec(select(Novel).where(Novel.id == novel_id)).first()
    print(novel_db)
    new_novel_data = novel.model_dump(exclude_unset=True)
    print(new_novel_data)
    update_novel = novel_db.model_copy(update=new_novel_data)
    print(update_novel)
    session.add(update_novel)
    session.commit()
    session.refresh(update_novel)
    return update_novel

def delete_novel(session: SessionDep, novel_id: int) -> Novel:
    novel = session.get(Novel, novel_id)
    session.delete(novel)
    session.commit()
    return novel


def create_chapter(session: SessionDep, chapter: Chapter_schema) -> Chapter:
    chapter =Chapter(number=chapter.number,title=chapter.title, content=chapter.content, novel_id=chapter.novel_id)
    session.add(chapter)    
    session.commit()
    session.refresh(chapter)
    return chapter

def update_chapter(session: SessionDep, chapter_id: int, chapter: Chapter) -> Chapter:
    # todo:fix update novels and chapter
    chapter_db = session.exec(select(Chapter).where(Chapter.id == chapter_id)).first()
    print(chapter_db)
    chapter_data = chapter.model_dump(exclude_unset=True)
    print(chapter_data)
    updated_chapter = chapter_db.model_copy(update=chapter_data)
    print(updated_chapter)
    session.add(updated_chapter)
    session.commit()
    session.refresh(updated_chapter)
    return updated_chapter

def delete_chapter(session: SessionDep, chapter_id: int) -> Chapter:
    chapter = session.get(Chapter, chapter_id)
    session.delete(chapter)
    session.commit()
    return chapter

# user.............
def create_user(session: SessionDep, user: user_schema) -> User:
    user = User(username=user.username)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Bookmarks.............
def add_bookmark(session: SessionDep, bookmark: bookmark_schema) -> Bookmark:
    bookmark = Bookmark(novel_id=bookmark.novel_id, user_id=bookmark.user_id)
    session.add(bookmark)
    session.commit()
    session.refresh(bookmark)
    return bookmark

def get_bookmarks(session: SessionDep, user_id: int) -> list[Bookmark]:
    bookmarks = session.exec(select(Bookmark).where(Bookmark.user_id == user_id)).all()
    return bookmarks

def delete_bookmark(session: SessionDep, bookmark_id: int) -> Bookmark:
    bookmark = session.exec(select(Bookmark).where(Bookmark.id == bookmark_id)).first()
    session.delete(bookmark)
    session.commit()
    return bookmark

# Rating.............
def add_rating(session: SessionDep, rating: rating_schema) -> Rating:
    rating = Rating(novel_id=rating.novel_id, user_id=rating.user_id, rating=rating.rating)
    session.add(rating)    
    session.commit()
    session.refresh(rating)
    return rating

def get_ratings(session: SessionDep, novel_id: int):
    ratings = session.exec(select(Rating).where(Rating.novel_id == novel_id)).all()
    total_rating = 0
    if len(ratings) == 0:
        return {"avg_rating": 0, "ratings": ratings}
    else:
        for rating in ratings:
            total_rating += rating.rating
        avg_rating = total_rating / len(ratings)
        print(avg_rating)
        # todo: add features for updating users rating
        context = {"avg_rating": avg_rating,           
                "ratings": ratings}
        return context


# total novel views..........
def add_novel_view(session: SessionDep, novel_id: int) -> NovelView:
    novel_views = session.exec(select(NovelView).where(NovelView.novel_id == novel_id)).first()
    print(novel_views)
    if novel_views is None:
        novel_views = NovelView(novel_id=novel_id, total_views=1)
    else:
        novel_views.total_views += 1
    session.add(novel_views)
    session.commit()
    session.refresh(novel_views)
    return novel_views


def get_novel_views(session: SessionDep, novel_id: int):
    novel_views = session.exec(select(NovelView).where(NovelView.novel_id == novel_id)).first()
    print(novel_views)
    return novel_views.total_views


# todossssssss
# TODO: the current genres model is not correct relationship
# TODO: edit get chaptes to get all chapters or some ammount of chapters
# todo: recommended novels, similar novels based on tags/genres 
# todo : reading history and last read chapter in cookie novel id and name and chapter id /use react /local storage (fe)
# todo :check read chapters color change (fe)

# todo check/test
# todo:add background task/repetitive task to change rank of novels once per day/hour
# todo: check sqlmodel and sql alchemy

# search............
def search_novels(session: SessionDep, query: str) -> list[Novel]:
    novels = session.exec(select(Novel).where(Novel.title.contains(query))).all()
    return novels


# rank of novels...........
def generate_rank_of_novels(session: SessionDep) -> dict:
    novels = session.exec(select(NovelView).order_by(NovelView.total_views.desc())).all()
    # print("calling rank of novels")
    # print(novels)
    rank = 1
    for novel in novels:
        print(novel.novel_id)
        get_novel_rank=session.exec(select(NovelRank).where(NovelRank.novel_id == novel.novel_id)).first()
        if get_novel_rank is None:
            new_novel_rank = NovelRank(novel_id=novel.novel_id, rank=rank)
        else:
            new_novel_rank = get_novel_rank.model_copy(update={"rank": rank})
       
        # print("novel_rank",new_novel_rank)
        session.add(new_novel_rank)
         
        rank += 1 #unable to update rank using above statement
    session.commit()
    # session.refresh(novels)

    return {'msg': "rank updated"}

def get_rank_of_novels(session: SessionDep) -> list[NovelRank]:
    print("calling rank of novels")
    # novels = session.exec(select(NovelRank).order_by(NovelRank.rank)).all()
    novels= session.exec(select(NovelRank)).all()
    print(novels)
    return novels

def get_rank_of_single_novel(session: SessionDep, novel_id: int) -> NovelRank:
    novel_rank = session.exec(select(NovelRank).where(NovelRank.novel_id == novel_id)).first() #todo :i'm fetching latest novel rank instance
    return novel_rank


#genres..............
def add_genre(session: SessionDep, genre: schemas.genre_schema) -> schemas.genre_schema:
    genre = Genre(novel_id=genre.novel_id, name=genre.name)
    session.add(genre)
    session.commit()
    session.refresh(genre)
    return genre

def get_genres(session: SessionDep, novel_id: int) -> list[genre_schema_out]:
    genres = session.exec(select(Genre).where(Genre.novel_id == novel_id)).all()
    return genres


#recommended novels..........
def get_recommended_novels(session: SessionDep, novel_id: int) -> list[Novel]:
    get_genre = session.exec(select(Genre).where(Genre.novel_id == novel_id)).all()
    print(get_genre)
    get_random_genre = random.choice(get_genre).name
    print(get_random_genre)
    recommended_novels = session.exec(select(Novel).where(Genre.name == get_random_genre)).all() #TODO not working  check how to fetch related items
    print(recommended_novels)
    return recommended_novels

# Home card..........
def get_home_cards(session: SessionDep,) -> list[schemas.HomeCard_schema]:
    novels = session.exec(select(Novel)).all()
    home_cards = []
    for novel in novels:
        # print("novel.id",novel.id)
        rating = get_ratings(session, novel.id)
        # print("rating",rating)
        recent_chapters = session.exec(select(Chapter).where(Chapter.novel_id == novel.id)).all()
        if len(recent_chapters) == 0:
            recent_ch_1 = None
            recent_ch_2 = None
        elif len(recent_chapters) == 1:
            recent_ch_1 = recent_chapters[0].number
            recent_ch_2 = None
        else:
            recent_ch_1 = recent_chapters[0].number
            recent_ch_2 = recent_chapters[1].number
        
        # print("recent_chapters",recent_chapters)
        home_cards.append(schemas.HomeCard_schema(novel_id=novel.id, title=novel.title, rating=rating["avg_rating"], chapter_num_1=recent_ch_1, chapter_num_2=recent_ch_2))
    return home_cards