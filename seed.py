from sqlalchemy.orm import Session
from models import Base, Movie, Genre
from database import engine

def seed_data(session: Session):
    # создаем жанры
    genre1 = Genre(name="Драма", description="Драматические фильмы")
    genre2 = Genre(name="Комедия", description="Комедийные фильмы")
    session.add_all([genre1, genre2])
    session.commit()

    # создаем фильмы
    movie1 = Movie(
        title="Фильм 1",
        year=2020,
        duration=120,
        rating=8.5,
        description="Описание фильма 1",
        genres=[genre1]
    )
    movie2 = Movie(
        title="Фильм 2",
        year=2018,
        duration=90,
        rating=7.2,
        description="Описание фильма 2",
        genres=[genre2]
    )

    session.add_all([movie1, movie2])
    session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    import sqlalchemy.orm
    session = sqlalchemy.orm.sessionmaker(bind=engine)()
    seed_data(session)
    session.close()
