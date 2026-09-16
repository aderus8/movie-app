from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Movie, User, Genre
from app.schemas import (
    MovieCreate,
    MovieUpdate,
    MovieResponse,
    GenreResponse,
    MovieListResponse
)
from app.security import get_current_user_id


router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)


@router.post("", response_model=MovieResponse, status_code=201)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):

    new_movie = Movie(
        title=movie.title,
        year=movie.year,
        rating=movie.rating,
        description=movie.description,
        poster_url=movie.poster_url
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    return new_movie


@router.get("", response_model=MovieListResponse)
def get_movies(
    search: str | None = None,
    genre: str | None = None,
    year_from: int | None = None,
    
    year_to: int | None = None,
    min_rating: float | None = None,
    sort_by: str = "title",
    order: str = "asc",
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Movie)

    if search:
        query = query.filter(
            Movie.title.ilike(f"%{search}%")
        )

    if genre:
        query = (
            query.join(Movie.genres)
            .filter(Genre.name.ilike(genre))
        )

    if year_from is not None:
        query = query.filter(
            Movie.year >= year_from
        )

    if year_to is not None:
        query = query.filter(
            Movie.year <= year_to
        )

    if min_rating is not None:
        query = query.filter(
            Movie.rating >= min_rating
        )

    sort_columns = {
        "title": Movie.title,
        "year": Movie.year,
        "rating": Movie.rating
    }

    sort_column = sort_columns.get(
        sort_by,
        Movie.title
    )

    if order == "desc":
        query = query.order_by(
            sort_column.desc()
        )
    else:
        query = query.order_by(
            sort_column.asc()
        )

    total = query.count()

    offset = (page - 1) * page_size

    movies = (
        query
        .offset(offset)
        .limit(page_size)
        .all()
    )

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "items": movies
    }


@router.get("/{movie_id}/similar", response_model=list[MovieResponse])
def get_similar_movies(
    movie_id: int,
    limit: int = Query(default=5, ge=1, le=20),
    db: Session = Depends(get_db)
):
    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    genre_ids = [
        genre.id
        for genre in movie.genres
    ]

    if not genre_ids:
        return []

    similar_movies = (
        db.query(Movie)
        .join(Movie.genres)
        .filter(
            Genre.id.in_(genre_ids),
            Movie.id != movie_id
        )
        .group_by(Movie.id)
        .order_by(
            func.count(Genre.id).desc(),
            Movie.rating.desc()
        )
        .limit(limit)
        .all()
    )

    return similar_movies


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not foudn"
        )

    return movie


@router.patch("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, movie_data: MovieUpdate, db: Session = Depends(get_db)):

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    update_data = movie_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(movie, field, value)

    db.commit()
    db.refresh(movie)

    return movie


@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not foudn"
        )

    db.delete(movie)
    db.commit()


@router.post("/{movie_id}/favourite", status_code=201)
def add_to_favourites(
    movie_id: int,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == current_user_id)
        .first()
    )

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    if movie in user.favourites:
        raise HTTPException(
            status_code=409,
            detail="Movie already in favourites"
        )

    user.favourites.append(movie)
    db.commit()

    return {
        "message": "Movie added to favourites"
    }


@router.delete("/{movie_id}/favourite", status_code=204)
def remove_from_favourites(
    movie_id: int,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == current_user_id)
        .first()
    )

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    if movie not in user.favourites:
        raise HTTPException(
            status_code=404,
            detail="Movie not in favourites"
        )

    user.favourites.remove(movie)
    db.commit()


@router.post("/{movie_id}/genres/{genre_id}", status_code=201)
def add_genre_to_movie(
    movie_id: int,
    genre_id: int,
    db: Session = Depends(get_db)
):

    movie = (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )

    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    genre = (
        db.query(Genre)
        .filter(Genre.id == genre_id)
        .first()
    )

    if genre is None:
        raise HTTPException(
            status_code=404,
            detail="Genre not found"
        )

    if genre in movie.genres:
        raise HTTPException(
            status_code=409,
            detail="Genre already assigned"
        )

    movie.genres.append(genre)
    db.commit()

    return {
        "message": "Genre added to movie"
    }