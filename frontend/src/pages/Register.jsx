import { useState } from "react";
import {
  Link,
  useNavigate
} from "react-router-dom";

import {
  registerUser,
  loginUser
} from "../services/api";

import "./Auth.css";

function Register() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [username, setUsername] =
    useState("");
  const [password, setPassword] =
    useState("");

  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");

    try {
      await registerUser(
        email,
        username,
        password
      );

      const loginData = await loginUser(
        email,
        password
      );

      localStorage.setItem(
        "token",
        loginData.access_token
      );

      navigate("/");
    } catch (error) {
      console.error(error);

      setError(
        error.response?.data?.detail ||
          "Registration failed"
      );
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-box">
        <h1>Create account</h1>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(event) =>
              setUsername(event.target.value)
            }
            required
          />

          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(event) =>
              setEmail(event.target.value)
            }
            required
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(event) =>
              setPassword(event.target.value)
            }
            required
          />

          {error && (
            <p className="auth-error">
              {error}
            </p>
          )}

          <button type="submit">
            Register
          </button>
        </form>

        <p className="auth-switch">
          Already have an account?{" "}
          <Link to="/login">
            Login
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Register;