from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import movies, ratings, users, reviews, genres


app = FastAPI(
    title="Movie API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(movies.router)
app.include_router(users.router)
app.include_router(ratings.router)
app.include_router(reviews.router)
app.include_router(genres.router)


@app.get("/")
def home():
    return {
        "message": "Movie API is running"
    }