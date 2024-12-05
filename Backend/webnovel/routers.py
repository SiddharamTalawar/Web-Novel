from fastapi import APIRouter, Depends
import crud as crud
import schemas as schemas
from schemas import Novel_schema, Chapter_schema, genre_schema, user_schema,bookmark_schema,rating_schema,NovelView_schema,HomeCard_schema
from models import Novel, Chapter, Bookmark, User, Rating, NovelView, NovelRank, Genre
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from models import SessionDep
from fastapi_utils.tasks import repeat_every
router = APIRouter()


@router.get("/novels/", response_model=list[Novel])
def read_novels(session: SessionDep) -> list[Novel]:
    return crud.get_novels(session)

@router.get("/novels/{novel_id}", response_model=Novel)
def read_novel(novel_id: int, session: SessionDep) -> Novel:
    return crud.get_novel(session, novel_id)

@router.post("/novels/")
def create_novel(novel: Novel_schema, session: SessionDep) -> Novel:
    return crud.create_novel(session, novel)

@router.patch("/novels/{novel_id}")
def update_novel(novel_id: int, novel: schemas.Novel_schema, session: SessionDep) -> schemas.Novel_schema:
    return crud.update_novel(session, novel_id, novel)

@router.delete("/novels/{novel_id}")
def delete_novel(novel_id: int, session: SessionDep) -> Novel:
    return crud.delete_novel(session, novel_id)

# chapters.............
@router.get("/novels/{novel_id}/chapters/", response_model=list[Chapter])
def read_chapters(novel_id: int, session: SessionDep) -> list[Chapter]:
    return crud.get_chapters(session, novel_id)

@router.get("/novels/chapters/{chapter_id}", response_model=Chapter)
def read_chapter( chapter_id: int, session: SessionDep) -> Chapter:
    return crud.get_chapter(session, chapter_id)

@router.post("/novels/{novel_id}/chapters/")
def create_chapter( chapter: Chapter_schema, session: SessionDep) -> Chapter:
    return crud.create_chapter(session, chapter)

@router.patch("/novels/{novel_id}/chapters/{chapter_id}")
def update_chapter(chapter_id: int, chapter: Chapter, session: SessionDep) -> Chapter:
    return crud.update_chapter(session, chapter_id, chapter)

@router.delete("/novels/{novel_id}/chapters/{chapter_id}")
def delete_chapter(chapter_id: int, session: SessionDep) -> Chapter:
    return crud.delete_chapter(session, chapter_id)

# users...............
@router.post("/users/")
def create_user(user: user_schema, session: SessionDep) -> User:
    return crud.create_user(session, user)

# bookmarks............
@router.get("/novels/read/bookmarks/{user_id}/", response_model=list[Bookmark])
def read_bookmarks(user_id: int, session: SessionDep) -> list[Bookmark]:
    return crud.get_bookmarks(session, user_id)

@router.post("/novels/{novel_id}/add/bookmarks/{user_id}/")
def create_bookmark(bookmark: bookmark_schema, session: SessionDep) -> Bookmark:
    return crud.add_bookmark(session, bookmark)

@router.delete("/novels/delete/bookmarks/")
def delete_bookmark(bookmark_id: int, session: SessionDep) -> Bookmark:
    return crud.delete_bookmark(session, bookmark_id)

# ratings..............
@router.get("/novels/{novel_id}/ratings/")
def read_ratings(novel_id: int, session: SessionDep):
    return crud.get_ratings(session, novel_id)

@router.post("/novels/{novel_id}/ratings/{user_id}/")
def create_rating(rating:rating_schema,session: SessionDep) -> Rating:
    return crud.add_rating(session, rating)

# total novel views..........
@router.get("/novels/{novel_id}/views/")
def read_views(novel_id: int, session: SessionDep) -> int:
    return crud.get_novel_views(session, novel_id)

@router.post("/novels/{novel_id}/views/")
def add_views(novel_id: int, session: SessionDep) -> NovelView:
    return crud.add_novel_view(session, novel_id)


# search............
@router.get("/search/")
def search(query: str, session: SessionDep) -> list[Novel]:
    return crud.search_novels(session, query)

# rank of novels...........
@router.get("/novels/rank/update/")
def generate_rank_of_novels(session: SessionDep) -> dict:
    return crud.generate_rank_of_novels(session)

@router.get("/novels/rank/")
def get_rank_of_novels(session: SessionDep) -> list[NovelRank]:
    return crud.get_rank_of_novels(session)

@router.get("/novels/{novel_id}/rank/")
def get_rank_of_single_novel(novel_id: int, session: SessionDep) -> NovelRank:
    return crud.get_rank_of_single_novel(session, novel_id)


#genrs..............
@router.get("/novels/{novel_id}/genres/")
def read_genres(novel_id: int, session: SessionDep) -> list[schemas.genre_schema_out]:
    return crud.get_genres(session, novel_id)

@router.post("/novels/create/genres/")
def create_genre( genre: schemas.genre_schema, session: SessionDep) -> schemas.genre_schema:
    return crud.add_genre(session, genre)

#recommended novels..........
@router.get("/novels/{novel_id}/recommended/")
def read_recommended_novels(novel_id: int, session: SessionDep) -> list[Novel]:
    return crud.get_recommended_novels(session, novel_id)

@router.get("/home-cards/")
def get_home_cards(session: SessionDep) -> list[HomeCard_schema]:
    return crud.get_home_cards(session)