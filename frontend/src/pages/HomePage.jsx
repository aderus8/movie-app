import { useEffect, useState } from "react";

import Hero from "../components/Hero";
import MovieSection from "../components/MovieSection";
import SearchBar from "../components/SearchBar";
import GenreFilter from "../components/GenreFilter";

import {
  getMovies,
  getGenres,
} from "../services/api";


function HomePage() {
  const [movies, setMovies] = useState([]);
  const [topRated, setTopRated] = useState([]);
  const [newest, setNewest] = useState([]);

  const [heroMovie, setHeroMovie] = useState(null);

  const [genres, setGenres] = useState([]);

  const [search, setSearch] = useState("");
  const [genre, setGenre] = useState("");


  useEffect(() => {
    const loadGenres = async () => {
      try {
        const data = await getGenres();
        setGenres(data);
      } catch (error) {
        console.error(
          "Error fetching genres:",
          error
        );
      }
    };

    loadGenres();
  }, []);


  useEffect(() => {
    const loadHomeSections = async () => {
      try {
        const [
          topRatedData,
          newestData,
        ] = await Promise.all([
          getMovies(
            "",
            "",
            "rating",
            "desc",
            6
          ),
          getMovies(
            "",
            "",
            "year",
            "desc",
            6
          ),
        ]);

        setTopRated(topRatedData);
        setNewest(newestData);

        const availableMovies =
          topRatedData.length > 0
            ? topRatedData
            : newestData;

        if (availableMovies.length > 0) {
          const randomIndex =
            Math.floor(
              Math.random() *
              availableMovies.length
            );

          setHeroMovie(
            availableMovies[randomIndex]
          );
        }
      } catch (error) {
        console.error(
          "Error fetching home sections:",
          error
        );
      }
    };

    loadHomeSections();
  }, []);


  useEffect(() => {
    const timer = setTimeout(() => {
      const loadMovies = async () => {
        try {
          const data = await getMovies(
            search,
            genre,
            "title",
            "asc",
            50
          );

          setMovies(data);
        } catch (error) {
          console.error(
            "Error fetching movies:",
            error
          );
        }
      };

      loadMovies();
    }, 400);

    return () => clearTimeout(timer);
  }, [search, genre]);


  return (
    <>
      <Hero
        movie={heroMovie}
        movies={topRated}
      />

      <main
        className="main-content"
        id="movies"
      >
        <MovieSection
          title="Top Rated"
          movies={topRated}
        />

        <MovieSection
          title="Newest"
          movies={newest}
        />

        <MovieSection
          title="All Movies"
          movies={movies}
          layout="grid"
        >
          <div className="filters">
            <SearchBar
              search={search}
              setSearch={setSearch}
            />

            <GenreFilter
              genre={genre}
              setGenre={setGenre}
              genres={genres}
            />
          </div>
        </MovieSection>
      </main>
    </>
  );
}


export default HomePage;