from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Movie, Rating
from app.schemas import RatingCreate
from app.security import get_current_user_id


router = APIRouter(
    prefix="/movies",
    tags=["Ratings"]
)

@router.post(
    "/{movie_id}/rating",
    status_code=201
)
def rate_movie(
    movie_id: int,
    rating_data: RatingCreate,
    current_user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    if rating_data.value < 1 or rating_data.value > 10:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 10"
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

    existing_rating = (
        db.query(Rating)
        .filter(
            Rating.user_id == current_user_id,
            Rating.movie_id == movie_id
        )
        .first()
    )

    if existing_rating is not None:
        existing_rating.value = rating_data.value

        db.commit()
        db.refresh(existing_rating)

        return {
            "message": "Rating updated",
            "rating": existing_rating.value
        }

    new_rating = Rating(
        value=rating_data.value,
        user_id=current_user_id,
        movie_id=movie_id
    )

    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)

    return {
        "message": "Rating created",
        "rating": new_rating.value
    }

@router.get("/{movie_id}/rating")
def get_movie_rating(
    movie_id: int,
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

    average, count = (
        db.query(
            func.avg(Rating.value),
            func.count(Rating.id)
        )
        .filter(Rating.movie_id == movie_id)
        .first()
    )

    return {
        "movie_id": movie_id,
        "average_rating": (
            round(float(average), 2)
            if average is not None
            else None
        ),
        "ratings_count": count
    }