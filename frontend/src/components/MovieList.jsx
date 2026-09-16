import MovieCard from "./MovieCard";
import "./MovieList.css";

function MovieList({ movies }) {
  if (movies.length === 0) {
    return (
      <p className="no-movies">
        No movies found
      </p>
    );
  }

  return (
    <div className="movie-list">
      {movies.map((movie) => (
        <MovieCard
          key={movie.id}
          movie={movie}
        />
      ))}
    </div>
  );
}

export default MovieList;