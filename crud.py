from sqlalchemy.orm import Session
from models import Movie, Genre
from schemas import MovieCreate, MovieUpdate
import shutil
import os
import uuid

def get_genres(db: Session, skip=0, limit=100):
    return db.query(Genre).offset(skip).limit(limit).all()

def create_genre(db: Session, genre):
    db_genre = Genre(name=genre.name, description=genre.description)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def get_movies(db: Session, skip=0, limit=100):
    return db.query(Movie).offset(skip).limit(limit).all()

def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(
        title=movie.title,
        year=movie.year,
        duration=movie.duration,
        rating=movie.rating,
        description=movie.description,
    )
    # Подгружаем жанры
    db_genres = db.query(Genre).filter(Genre.id.in_(movie.genre_ids)).all()
    db_movie.genres = db_genres
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def update_movie(db: Session, movie_id: int, movie_update: MovieUpdate):
    movie = get_movie(db, movie_id)
    if not movie:
        return None
    if movie_update.title is not None:
        movie.title = movie_update.title
    if movie_update.year is not None:
        movie.year = movie_update.year
    if movie_update.duration is not None:
        movie.duration = movie_update.duration
    if movie_update.rating is not None:
        movie.rating = movie_update.rating
    if movie_update.description is not None:
        movie.description = movie_update.description
    if movie_update.genre_ids is not None:
        genres = db.query(Genre).filter(Genre.id.in_(movie_update.genre_ids)).all()
        movie.genres = genres
    db.commit()
    db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int):
    movie = get_movie(db, movie_id)
    if not movie:
        return False
    db.delete(movie)
    db.commit()
    return True

def update_movie_poster(db: Session, movie_id: int, filename: str):
    movie = get_movie(db, movie_id)
    if not movie:
        return None
    movie.poster_url = filename
    db.commit()
    db.refresh(movie)
    return movie
