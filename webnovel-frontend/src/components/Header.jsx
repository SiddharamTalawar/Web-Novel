import { IoSearch } from "react-icons/io5";
import { AiOutlineCaretRight } from "react-icons/ai";
import "../styles/Header.css";
import logo from "../assets/BoxNovelNEW image.png";
import { useState } from "react";
import { Link } from "react-router-dom";
function Header() {
  const [showHiddenGenres, setShowHiddenGenres] = useState(false);
  const [showSearchBar, setShowSearchBar] = useState(false);

  const handleShowSearchBar = () => setShowSearchBar(!showSearchBar);

  return (
    <div className="header">
      <div className="header-top">
        <div className="header-left">
          <div className="site-logo mouse-hover">
            <Link to="/">
              <img src={logo} alt="site-logo" />
            </Link>
          </div>
        </div>
        <div className="header-center"></div>
        <div className="header-right">
          <div className="search mouse-hover" onClick={handleShowSearchBar}>
            <i>
              <IoSearch />
            </i>
          </div>
          <div className="advanced-search mouse-hover">Advanced</div>
        </div>
      </div>
      <div className="navbar ">
        <ul>
          <li>Action</li>
          <li>Adventure</li>
          <li>Fantasy</li>
          <li>Romance</li>
          <li>Harem</li>
          <li
            className="more-genres"
            onClick={() => setShowHiddenGenres(!showHiddenGenres)}
          >
            More{" "}
            <i className="right-arrow">
              <AiOutlineCaretRight />
            </i>
            {showHiddenGenres && (
              <div className="hidden-genres">
                <ul>
                  <li>Comedy</li>
                  <li>Drama</li>
                  <li>Historical</li>
                  <li>Horror</li>
                  <li>Mystery</li>
                  <li>Psychological</li>
                  <li>Sci-Fi</li>
                  <li>Slice of Life</li>
                </ul>
              </div>
            )}
          </li>
        </ul>
        <div className="signup">
          <button className="signup-button">Sign Up</button>
          <button className="signup-button">Log In</button>
        </div>
      </div>

      {showSearchBar && (
        <div className="search-bar">
          <label htmlFor="search"></label>
          <input type="text" id="search" placeholder="Search" />
          <button>
            <i>
              <IoSearch />
            </i>
          </button>
        </div>
      )}
    </div>
  );
}

export default Header;
