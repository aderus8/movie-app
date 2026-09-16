import { useEffect, useState } from "react";

import MovieList from "../components/MovieList";
import { getFavourites } from "../services/api";

import "./MyList.css";

function MyList() {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const loadFavourites = async () => {
      try {
        const data = await getFavourites();
        setMovies(data);
      } catch (error) {
        console.error(error);

        setError(
          error.response?.data?.detail ||
            "Could not load favourites"
        );
      } finally {
        setLoading(false);
      }
    };

    loadFavourites();
  }, []);

  if (loading) {
    return (
      <div className="my-list-page">
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="my-list-page">
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div className="my-list-page">
      <h1>My List</h1>

      <MovieList movies={movies} />
    </div>
  );
}

export default MyList;