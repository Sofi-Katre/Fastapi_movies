from database import Base
from sqlalchemy import Column, Integer, String, Date,Table, ForeignKey

student_course = Table("movie_genre", Base.metadata,
                       Column("movie_id", ForeignKey("movies.id"), primary_key=True),
                       Column("genre_id", ForeignKey("genres.id"), primary_key=True))


class Genre(Base):
    __tablename__="genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String(80), unique=True)
    genre_description = Column(String(255))

class Movie(Base):
    __tablename__="movies"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_name = Column(String(255))
    movie_year = Column(Integer)
    movie_time = Column(Integer)
    movie_rate = Column(Integer)
    movie_description = Column(String(255))
    movie_poster = Column(String(255))
    movie_add_date = Column(Date)
