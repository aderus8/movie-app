function GenreFilter({
  genre,
  setGenre,
  genres
}) {
  return (
    <select
      value={genre}
      onChange={(event) =>
        setGenre(event.target.value)
      }
    >
      <option value="">
        All genres
      </option>

      {genres.map((item) => (
        <option
          key={item.id}
          value={item.name}
        >
          {item.name}
        </option>
      ))}
    </select>
  );
}

export default GenreFilter;