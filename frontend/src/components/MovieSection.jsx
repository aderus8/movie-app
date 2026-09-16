import MovieList from "./MovieList";

function MovieSection({
  title,
  movies,
  layout = "row",
  children,
}) {
  return (
    <section className="movie-section">
      <div className="movie-section-header">
        <h2 className="section-title">
          {title}
        </h2>

        {children}
      </div>

      <MovieList
        movies={movies}
        layout={layout}
      />
    </section>
  );
}

export default MovieSection;