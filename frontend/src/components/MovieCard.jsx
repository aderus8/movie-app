import { Link } from "react-router-dom";
import "./MovieCard.css";

function MovieCard({ movie }) {
    const poster = movie.poster_url
        ? movie.poster_url
        : "/images/no-poster.jpg";

    return (
        <Link
            to={`/movies/${movie.id}`}
            className="movie-card"
        >
            <div className="movie-poster">
                <img
                    src={poster}
                    alt={movie.title}
                />

                <div className="movie-card-overlay" />

                {movie.rating && (
                    <span className="movie-rating">
                        ★ {Number(movie.rating).toFixed(1)}
                    </span>
                )}

                <div className="movie-card-action">
                    View movie
                </div>
            </div>

            <div className="movie-card-info">
                <h3>{movie.title}</h3>

                <div className="movie-meta">
                    <span>{movie.year}</span>

                    {movie.genres?.length > 0 && (
                        <>
                            <span className="movie-dot">•</span>

                            <span>
                                {movie.genres[0].name}
                            </span>
                        </>
                    )}
                </div>
            </div>
        </Link>
    );
}

export default MovieCard;