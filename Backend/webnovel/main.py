from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Novel, Chapter, get_session, create_db_and_tables
from models import SessionDep
from fastapi_utils.tasks import repeat_every
import crud as crud
# from scraper import get_soup
from contextlib import asynccontextmanager
# import events as events
from events import  generate_rank_of_novels
from fastapi.middleware.cors import CORSMiddleware

from routers import router
@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await generate_rank_of_novels()
    yield  #Note this is important always add yeild when you are using asynccontextmanager else you will get error TypeError: 'coroutine' object is not an async iterator
    

app = FastAPI(lifespan=lifespan)




origins = [
    "http://localhost:5173",
    # "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
@app.get("/")
def create_tables():

    create_db_and_tables()

# @app.on_event("startup")
# @repeat_every(seconds=60 * 2)  # 1 hour
# def generate_rank_of_novels(session: SessionDep) -> dict:
#     return crud.generate_rank_of_novels(session)
# @app.get("/scrape") 
# async def scrape():
#     return get_soup()
   
# class Novel(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     title: str
#     description: str
#     author: str

# class Chapter(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     number: int 
#     content: str
#     novel_id: int = Field( foreign_key="novel.id")
#     # novel: Novel | None = None

# @app.post("/")
# async def root(novel: Novel):
#     return novel