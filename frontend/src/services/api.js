import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8001",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

export const getMovies = async (
  search = "",
  genre = "",
  sortBy = "title",
  order = "asc",
  pageSize = 50
) => {
  const response = await api.get("/movies", {
    params: {
      search: search || undefined,
      genre: genre || undefined,
      sort_by: sortBy,
      order: order,
      page_size: pageSize,
    },
  });

  return response.data.items;
};

export const getGenres = async () => {
  const response = await api.get("/genres");

  return response.data;
};

export const loginUser = async (
  email,
  password
) => {
  const response = await api.post(
    "/users/login",
    {
      email,
      password,
    }
  );

  return response.data;
};

export const registerUser = async (
  email,
  username,
  password
) => {
  const response = await api.post(
    "/users/register",
    {
      email,
      username,
      password,
    }
  );

  return response.data;
};

export const getCurrentUser = async () => {
  const response = await api.get("/users/me");

  return response.data;
};

export const getFavourites = async () => {
  const response = await api.get(
    "/users/me/favourites"
  );

  return response.data;
};

export const addFavourite = async (
  movieId
) => {
  const response = await api.post(
    `/movies/${movieId}/favourite`
  );

  return response.data;
};

export const removeFavourite = async (
  movieId
) => {
  const response = await api.delete(
    `/movies/${movieId}/favourite`
  );

  return response.data;
};

export const rateMovie = async (
  movieId,
  value
) => {
  const response = await api.post(
    `/movies/${movieId}/rating`,
    {
      value,
    }
  );

  return response.data;
};

export const getMovieRating = async (
  movieId
) => {
  const response = await api.get(
    `/movies/${movieId}/rating`
  );

  return response.data;
};

export default api;