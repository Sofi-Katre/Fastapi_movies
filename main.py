from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import os
import uuid

from database import SessionLocal, init_db
import models
import schemas
import crud
from utils import save_image

app = FastAPI()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    init_db()

# --- Жанры ---
@app.get("/genres", response_model=List[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_genres(db, skip=skip, limit=limit)

@app.post("/genres", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db, genre)

# --- Фильмы ---
@app.get("/movies", response_model=List[schemas.Movie])
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit)

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return movie

@app.post("/movies", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@app.put("/movies/{movie_id}", response_model=schemas.Movie)
def update_movie(movie_id: int, movie_update: schemas.MovieUpdate, db: Session = Depends(get_db)):
    movie = crud.update_movie(db, movie_id, movie_update)
    if not movie:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return movie

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    success = crud.delete_movie(db, movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return {"detail": "Фильм удален"}

@app.put("/movies/{movie_id}/image")
def update_movie_image(movie_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Валидация файла
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Недопустимый тип файла")
    # Сохраняем изображение (обработка по имени и размеру)
    filename = save_image(file)
    updated_movie = crud.update_movie_poster(db, movie_id, filename)
    if not updated_movie:
        raise HTTPException(status_code=404, detail="Фильм не найден")
    return {"poster_url": filename}

