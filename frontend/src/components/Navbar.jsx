import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
    const navigate = useNavigate();
    const token = localStorage.getItem("token");

    const logout = () => {
        localStorage.removeItem("token");
        navigate("/login");
    };

    return (
        <nav className="navbar">
            <Link to="/" className="navbar-logo">
                MOVIES<span></span>
            </Link>

            <div className="navbar-links">
                <Link to="/">Discover</Link>

                {token && (
                    <Link to="/favourites">
                        My List
                    </Link>
                )}
            </div>

            <div className="navbar-actions">
                {token ? (
                    <button
                        className="navbar-logout"
                        onClick={logout}
                    >
                        Log out
                    </button>
                ) : (
                    <>
                        <Link
                            to="/login"
                            className="navbar-login"
                        >
                            Sign in
                        </Link>

                        <Link
                            to="/register"
                            className="navbar-register"
                        >
                            Join now
                        </Link>
                    </>
                )}
            </div>
        </nav>
    );
}

export default Navbar;