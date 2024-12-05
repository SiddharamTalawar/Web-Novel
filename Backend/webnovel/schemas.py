from pydantic import BaseModel


class Novel_schema(BaseModel):
    title: str|None
    description: str|None
    author: str|None
    # genres: list[str]|None
    # views: int|None
    # rating: float|None
    # rank: int|None


class Chapter_schema(BaseModel):
    number: int
    title: str
    content: str
    novel_id: int


class genre_schema(BaseModel):
    novel_id: int
    name: str
class genre_schema_out(BaseModel):
    name: str
class user_schema(BaseModel):
    username : str

class bookmark_schema(BaseModel):
    novel_id: int
    user_id: int

class rating_schema(BaseModel):
    novel_id: int
    user_id: int
    rating: int

class NovelView_schema(BaseModel):
    novel_id: int

class HomeCard_schema(BaseModel):
    novel_id: int|None
    title: str|None
    rating: float|None
    chapter_num_1 : int|None
    chapter_num_2 : int|None