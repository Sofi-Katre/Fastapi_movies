from pydantic import BaseModel, HttpUrl, Field, validator
from typing import List, Optional

class GenreBase(BaseModel):
    name: str
    description: Optional[str]

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    title: str
    year: Optional[int]
    duration: Optional[int]
    rating: Optional[float] = Field(0, ge=0, le=10)
    description: Optional[str]
    genre_ids: List[int]

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    poster_url: Optional[HttpUrl]
    date_added: str
    genres: List[Genre]

    class Config:
        orm_mode = True

class MovieUpdate(BaseModel):
    title: Optional[str]
    year: Optional[int]
    duration: Optional[int]
    rating: Optional[float] = Field(None, ge=0, le=10)
    description: Optional[str]
    genre_ids: Optional[List[int]]

class MovieImageUpdate(BaseModel):
    # Эта схема не нужна, так как мы будем получать файл
    pass
