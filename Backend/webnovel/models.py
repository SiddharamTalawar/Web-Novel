from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
from fastapi import Depends
from schemas import genre_schema


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

class Novel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    author: str
    genres :str|None
    views: int|None
    rating: float|None
    rank: int|None


class Chapter(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    number: int 
    title: str 
    content: str
    novel_id: int  = Field(default=None, foreign_key="novel.id")
    read: bool = False        #to check if chapter is read and change the color of it in frontend
    # TODO: add chapter title field 

class Bookmark(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="novel.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")
    # novel: Novel | None = None

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str


class Rating(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="novel.id")
    user_id: int | None = Field(default=None, foreign_key="user.id")
    rating: int


# total novel views..........
class NovelView(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="novel.id")
    # user_id: int | None = Field(default=None, foreign_key="user.id")
    total_views: int | None


# Genres..................
class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="novel.id")
    name: str


# todo: add genres to novel model

# novel rank.................
class NovelRank(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    novel_id: int | None = Field(default=None, foreign_key="novel.id")
    rank: int