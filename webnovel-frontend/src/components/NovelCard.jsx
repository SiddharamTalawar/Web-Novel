import NoveCardImg from "../assets/NoveCardImg.jpeg";
import "../styles/novelCard.css";
import StarRating from "./StarRating";
import { IoBookmark } from "react-icons/io5";
import { useNavigate } from "react-router-dom";
function NovelCard({
  novel_id,
  author,
  rating,
  rank,
  views,
  genres,
  chapters,
}) {
  const uniqueGenres = (genres) => [...new Set(genres)];
  const navigate = useNavigate();
  // function to load chapter
  const handleClick = (chapter) => {
    navigate("/chapter/", {
      state: {
        chapters: chapters,
        chapter: chapter,
      },
    });
  };
  return (
    <>
      <div className="novel-card">
        <div className="novel-card-img">
          <img src={NoveCardImg} alt="novel-card-img" />
        </div>
        <div className="novel-card-content">
          <div className="novel-card-left">
            <div className="novel-card-rating">
              <StarRating rating={rating.avg_rating} />
            </div>
            <div className="novel-card-text">
              <p>
                {" "}
                <span className="bold-text">Rating</span>{" "}
                <span className="rating">
                  Average {rating.avg_rating} / 5 out of 30
                </span>
              </p>
              <p>
                <span className="bold-text">Rank</span>{" "}
                <span className="rank">
                  {rank}, it has {views} monthly views
                </span>
              </p>
              <p>
                <span className="bold-text">Author</span>{" "}
                <span className="author">{author}</span>
              </p>
              <p>
                <span className="bold-text">Genre(s)</span>{" "}
                <span className="genres">{uniqueGenres(genres)}</span>
              </p>
              <p>
                <span className="bold-text">Type</span>{" "}
                <span className="type">Chinese Webnovel</span>
              </p>
              <p>
                <span className="bold-text">Tag(s)</span>{" "}
                <span className="tags">CHINESE NOVEL </span>
              </p>
            </div>
          </div>
          <div className="novel-card-right">
            <div className="novel-status">
              <span className="bold-text">Status</span> ongoin
            </div>
            <div className="bookmark-button">
              <i>
                <IoBookmark />
              </i>
              <p>100 users bookmarked this</p>
            </div>
            <div className="read-buttons">
              <button
                className="read-button"
                onClick={() => handleClick(chapters[0])}
              >
                Read First
              </button>
              <button
                className="read-button"
                onClick={() => handleClick(chapters[chapters.length - 1])}
              >
                Read Last
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default NovelCard;
