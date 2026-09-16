from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Movie, Review
from app.schemas import ReviewCreate, ReviewResponse
from app.security import get_current_user_id


router = APIRouter(
    prefix="/movies",
    tags=["Reviews"]
)

@router.post("/{movie_id}/reviews", response_model=ReviewResponse, status_code=201)
def create_review(movie_id: int, review_data: ReviewCreate, current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):

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

    new_review = Review(
        content=review_data.content,
        user_id=current_user_id,
        movie_id=movie_id
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review

@router.get("/{movie_id}/reviews", response_model=list[ReviewResponse])
def get_movie_reviews(movie_id:int, db:Session=Depends(get_db)):

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

    reviews = (
        db.query(Review)
        .filter(Review.movie_id == movie_id)
        .all()
    )

    return reviews

@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(review_id: int, current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):

    review = (
        db.query(Review)
        .filter(Review.id == review_id)
        .first()
    )

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    if review.user_id != current_user_id:
        raise HTTPException(
            status_code=403,
            detail="This user cannot delet this reveivs"
        )

    db.delete(review)
    db.commit()