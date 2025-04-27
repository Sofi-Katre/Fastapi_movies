from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# Связь многие-ко-многим между фильмами и жанрами
movie_genre_association = Table(
    'movie_genre_association',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    duration = Column(Integer)  # мин
    rating = Column(Float)
    description = Column(String, nullable=True)
    poster_url = Column(String, nullable=True)
    date_added = Column(DateTime(timezone=True), server_default=func.now())

    genres = relationship('Genre', secondary=movie_genre_association, back_populates='movies')

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    movies = relationship('Movie', secondary=movie_genre_association, back_populates='genres')
