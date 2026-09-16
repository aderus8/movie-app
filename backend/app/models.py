from sqlalchemy import Boolean, Column, Float, Integer, String, Text, ForeignKey, Table, UniqueConstraint, DateTime
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


user_favourites = Table(
"user_favourites",
    Base.metadata,
    Column(
        "user_id",
        ForeignKey("users.id"),
        primary_key=True
    ),
    Column(
        "movie_id",
        ForeignKey("movies.id"),
        primary_key=True
    )
)

movie_genres = Table(
    "movie_genres",
    Base.metadata,
    Column(
        "movie_id",
        ForeignKey("movies.id"),
        primary_key=True
    ),
    Column(
        "genre_id",
        ForeignKey("genres.id"),
        primary_key=True
    )
)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=True)
    description = Column(Text, nullable=True)
    poster_url = Column(String(500), nullable=True)

    genres = relationship(
        "Genre",
        secondary=movie_genres,
        back_populates="movies"
    )

    favourited_by = relationship(
        "User",
        secondary=user_favourites,
        back_populates="favourites"
    )
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    favourites = relationship(
        "Movie",
        secondary=user_favourites,
        back_populates="favourited_by"
    )

class Rating(Base):

    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Integer, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    movie_id = Column(
        Integer,
        ForeignKey("movies.id"),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "movie_id",
            name="unique_user_movie_rating"
        ),
    )

    user = relationship("User")
    movie = relationship("Movie")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    content = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    movie_id = Column(
        Integer,
        ForeignKey("movies.id"),
        nullable=False
    )

    user = relationship("User")
    movie = relationship("Movie")





class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(
        String(100),
        unique=True,
        nullable=False
    )

    movies = relationship(
        "Movie",
        secondary=movie_genres,
        back_populates="genres"
    )