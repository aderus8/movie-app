import { Link } from "react-router-dom";

import "./Hero.css";


function Hero({ movie, movies = [] }) {
  return (
    <section className="hero">

      <div className="hero-content">

        <div className="hero-copy">
          <span className="hero-label">
            CURATED FOR MOVIE LOVERS
          </span>

          <h1>
            Stories worth
            <br />
            getting lost in.
          </h1>

          <p className="hero-description">
            Discover movies, build your personal
            watchlist and find your next favourite
            story.
          </p>

          <div className="hero-actions">
            <a
              href="#movies"
              className="hero-primary"
            >
              Explore movies
            </a>

            <Link
              to="/favourites"
              className="hero-secondary"
            >
              My watchlist
            </Link>
          </div>

          {movie && (
            <div className="hero-featured">
              <span>FEATURED</span>

              <strong>
                {movie.title}
              </strong>

              <p>
                {movie.year}

                {movie.rating && (
                  <>
                    {" "}·{" "}
                    ★ {Number(movie.rating).toFixed(1)}
                  </>
                )}
              </p>
            </div>
          )}
        </div>


        {movies.length > 0 && (
          <div className="hero-showcase">

            <div className="showcase-heading">
              <div>
                <span>TOP PICKS</span>

                <h2>
                  Popular right now
                </h2>
              </div>

              <span className="showcase-count">
                01 — 06
              </span>
            </div>


            <div className="hero-movies">
              {movies
                .slice(0, 6)
                .map((item, index) => (
                  <Link
                    key={item.id}
                    to={`/movies/${item.id}`}
                    className="hero-movie-card"
                  >
                    <img
                      src={
                        item.poster_url ||
                        "/images/no-poster.jpg"
                      }
                      alt={item.title}
                    />

                    <div className="hero-movie-overlay" />

                    <span className="hero-movie-number">
                      {String(index + 1).padStart(
                        2,
                        "0"
                      )}
                    </span>

                    {item.rating && (
                      <span className="hero-movie-rating">
                        ★{" "}
                        {Number(
                          item.rating
                        ).toFixed(1)}
                      </span>
                    )}

                    <div className="hero-movie-info">
                      <strong>
                        {item.title}
                      </strong>

                      <span>
                        {item.year}
                      </span>
                    </div>
                  </Link>
                ))}
            </div>

          </div>
        )}

      </div>

      <div className="hero-bottom-fade" />
    </section>
  );
}


export default Hero;