import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import api, {
  addFavourite,
  removeFavourite,
  getFavourites,
  rateMovie,
  getMovieRating,
} from "../services/api";

import "./MovieDetails.css";

function MovieDetails() {
  const { id } = useParams();

  const [movie, setMovie] = useState(null);
  const [error, setError] = useState("");

  const [isFavourite, setIsFavourite] = useState(false);
  const [favouriteMessage, setFavouriteMessage] = useState("");

  const [userRating, setUserRating] = useState("");
  const [averageRating, setAverageRating] = useState(null);
  const [ratingCount, setRatingCount] = useState(0);
  const [ratingMessage, setRatingMessage] = useState("");

  const token = localStorage.getItem("token");

  useEffect(() => {
    const loadMovie = async () => {
      try {
        const response = await api.get(`/movies/${id}`);

        setMovie(response.data);
      } catch (error) {
        console.error(error);

        setError(
          error.response?.data?.detail ||
            "Movie not found"
        );
      }
    };

    loadMovie();
  }, [id]);

  useEffect(() => {
    const loadRating = async () => {
      try {
        const data = await getMovieRating(id);

        setAverageRating(data.average_rating);
        setRatingCount(data.rating_count);
      } catch (error) {
        console.error(
          "Could not load rating:",
          error
        );
      }
    };

    loadRating();
  }, [id]);

  useEffect(() => {
    const checkFavourite = async () => {
      if (!token) {
        return;
      }

      try {
        const favourites = await getFavourites();

        const exists = favourites.some(
          (favouriteMovie) =>
            favouriteMovie.id === Number(id)
        );

        setIsFavourite(exists);
      } catch (error) {
        console.error(
          "Could not load favourites:",
          error
        );
      }
    };

    checkFavourite();
  }, [id, token]);

  const handleAddFavourite = async () => {
    if (!movie) {
      return;
    }

    if (!token) {
      setFavouriteMessage(
        "You need to log in first"
      );

      return;
    }

    try {
      await addFavourite(movie.id);

      setIsFavourite(true);

      setFavouriteMessage(
        "Added to My List"
      );
    } catch (error) {
      console.error(error);

      setFavouriteMessage(
        error.response?.data?.detail ||
          "Could not add movie"
      );
    }
  };

  const handleRemoveFavourite = async () => {
    if (!movie) {
      return;
    }

    try {
      await removeFavourite(movie.id);

      setIsFavourite(false);

      setFavouriteMessage(
        "Removed from My List"
      );
    } catch (error) {
      console.error(error);

      setFavouriteMessage(
        error.response?.data?.detail ||
          "Could not remove movie"
      );
    }
  };

  const handleRateMovie = async () => {
    if (!token) {
      setRatingMessage(
        "You need to log in first"
      );

      return;
    }

    const numericRating = Number(userRating);

    if (
      numericRating < 1 ||
      numericRating > 10
    ) {
      setRatingMessage(
        "Rating must be between 1 and 10"
      );

      return;
    }

    try {
      await rateMovie(
        movie.id,
        numericRating
      );

      setRatingMessage(
        "Rating saved"
      );

      const updatedRating =
        await getMovieRating(movie.id);

      setAverageRating(
        updatedRating.average_rating
      );

      setRatingCount(
        updatedRating.rating_count
      );
    } catch (error) {
      console.error(error);

      setRatingMessage(
        error.response?.data?.detail ||
          "Could not save rating"
      );
    }
  };

  if (error) {
    return (
      <div className="details-message">
        {error}
      </div>
    );
  }

  if (!movie) {
    return (
      <div className="details-message">
        Loading...
      </div>
    );
  }

  return (
    <div
      className="movie-details"
      style={{
        backgroundImage: movie.poster_url
          ? `url(${movie.poster_url})`
          : "none",
      }}
    >
      <div className="details-background"></div>

      <div className="details-content">
        <div className="details-poster-container">
          {movie.poster_url ? (
            <img
              src={movie.poster_url}
              alt={movie.title}
              className="details-poster"
            />
          ) : (
            <div className="details-placeholder">
              {movie.title}
            </div>
          )}
        </div>

        <div className="details-info">
          <h1>{movie.title}</h1>

          <div className="details-meta">
            <span>{movie.year}</span>

            {movie.rating !== null && (
              <span>
                External: ⭐ {movie.rating}
              </span>
            )}
          </div>

          <div className="user-rating-summary">
            <strong>User rating:</strong>

            {averageRating !== null ? (
              <span>
                ⭐ {Number(averageRating).toFixed(1)}
                {" "}
                ({ratingCount} ratings)
              </span>
            ) : (
              <span>No ratings yet</span>
            )}
          </div>

          <p className="details-description">
            {movie.description ||
              "No description available."}
          </p>

          <div className="details-actions">
            {token ? (
              !isFavourite ? (
                <button
                  onClick={handleAddFavourite}
                  className="details-button"
                >
                  + My List
                </button>
              ) : (
                <button
                  onClick={handleRemoveFavourite}
                  className="details-button secondary"
                >
                  Remove from My List
                </button>
              )
            ) : (
              <button
                onClick={handleAddFavourite}
                className="details-button"
              >
                + My List
              </button>
            )}

            {favouriteMessage && (
              <p className="favourite-message">
                {favouriteMessage}
              </p>
            )}
          </div>

          <div className="rating-section">
            <h3>Rate this movie</h3>

            <div className="rating-controls">
              <select
                value={userRating}
                onChange={(event) =>
                  setUserRating(
                    event.target.value
                  )
                }
              >
                <option value="">
                  Choose rating
                </option>

                {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(
                  (value) => (
                    <option
                      key={value}
                      value={value}
                    >
                      {value}
                    </option>
                  )
                )}
              </select>

              <button
                onClick={handleRateMovie}
                className="details-button"
              >
                Save rating
              </button>
            </div>

            {ratingMessage && (
              <p className="rating-message">
                {ratingMessage}
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default MovieDetails;