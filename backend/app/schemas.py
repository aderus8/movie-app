from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

class MovieCreate(BaseModel):
    title: str
    year:int
    rating: float | None = None
    description: str | None = None
    poster_url: str | None = None

class MovieResponse(MovieCreate):
    id: int

    class Config: 
        from_attributes = True

class MovieUpdate(BaseModel):
    title: str | None = None
    year: int | None = None
    rating: float | None = None
    description: str | None = None
    poster_url: str | None = None

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class RatingCreate(BaseModel):
    value: int

class ReviewCreate(BaseModel):
    content: str


class ReviewResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    user_id: int
    movie_id: int

    model_config = ConfigDict(from_attributes=True)

class GenreCreate(BaseModel):
    name: str


class GenreResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class MovieListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[MovieResponse]