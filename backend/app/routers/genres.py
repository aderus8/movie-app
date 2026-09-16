from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Genre, Movie
from app.schemas import GenreCreate, GenreResponse


router = APIRouter(
    prefix="/genres",
    tags=["Genres"]
)


@router.post("", response_model=GenreResponse, status_code=201)
def create_genre(genre_data: GenreCreate, db: Session = Depends(get_db)):

    exisiting_genre = (
        db.query(Genre)
        .filter(Genre.name == genre_data.name)
        .first()
    )

    if exisiting_genre is not None:
        raise HTTPException(
            status_code=400,
            detail="Genre alraedy exists"
        )

    new_genre = Genre(
        name=genre_data.name
    )

    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)

    return new_genre


@router.get("", response_model=list[GenreResponse])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()

