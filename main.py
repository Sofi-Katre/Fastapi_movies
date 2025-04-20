from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd


app=FastAPI()

# Жанры
@app.get('/genres', response_model=List[pyd.BaseGenre])
def get_all_genres(db:Session=Depends(get_db)):
    genres = db.query(m.Genre).all()
    return genres

@app.post("/genres")
def movie_product(genre:pyd.CreateGenre, db:Session=Depends(get_db)):
    genre_db = m.Genre()
    genre_db.genre_name = genre.genre_name

    db.add(genre_db)
    db.commit()
    return genre_db

# Фильмы
@app.get("/movies", response_model=List[pyd.BaseMovie])
def get_all_movies(db:Session=Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id:int, db:Session=Depends(get_db)):
    movie = db.query(m.Movie).filter(
        m.Movie.id==movie_id
    ).first()
    if not movie:
        raise HTTPException(404, 'Фильм не найдена')
    return movie

@app.post("/movies")
def movie_add(genre:pyd.CreateMovie, db:Session=Depends(get_db)):
    movie_db = m.Movie()
    movie_db.movie_name = genre.movie_name
    db.add(movie_db)
    db.commit()
    return movie_db

@app.delete("/movies/{movie_id}")
def delete_product(movie_id:int, db:Session=Depends(get_db)):
    movie = db.query(m.Movie).filter(
        m.Movie.id==movie_id
    ).first()
    if not movie:
        raise HTTPException(404, 'Фильм не найден')
    db.delete(movie)
    db.commit()
    return {'detail': "Фильм удален"}

@app.put("/movies/{movie_id}", response_model=List[pyd.BaseMovie])
def get_all_movies(db:Session=Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies


@app.put("/movies/{movie_id}/movie_poster", response_model=List[pyd.BaseMovie])
def get_all_movies(db:Session=Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies