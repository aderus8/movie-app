function SearchBar({ search, setSearch }) {
  return (
    <input
      type="text"
      placeholder="Search movies..."
      value={search}
      onChange={(event) => setSearch(event.target.value)}
    />
  );
}

export default SearchBar;