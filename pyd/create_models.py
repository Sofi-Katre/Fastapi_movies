from pydantic import BaseModel, Field
from datetime import date 


class CreateGenre(BaseModel):
    genre_name:str=Field(min_length=3, max_length=80, example='Детектив')
    genre_description: str=Field(max_length=255, example='Артур Конан Доиль создал свое первое произвдение о Шерлоке еще до четкого зарождения жанра детектив')


class CreateMovie(BaseModel):
    movie_name:str=Field(min_length=3, max_length=80, example='Возвращение Шерлока Холмса')
    movie_year: int=Field(min = 1900, max = 3000, example=2005)
    movie_time: int=Field(max = 180, example=55)
    movie_rate: int=Field(min = 0, max = 10, example=5)
    movie_description: str=Field(max_length=255, example='Всеми любимый Шерлок снова в деле, и Доктор Уатсон, его друг, поможет с очередным раскрытием преступления')
    movie_poster: str=Field(max_length=255)
    movie_add_date: date=Field(example='2020-04-03')
