import novelImg from "../assets/novelImg.jpg";
// import supremetamer from "../assets/supreme-Tamer.jpeg";
import "../styles/HomeCard.css";
import StarRating from "./StarRating";
import { useNavigate } from "react-router-dom";
function HomeCard({ novel }) {
  // function storeHistory(key, value) {
  //   let d = new Date();
  //   let stroageObj = {
  //     chapter: value,
  //     time: d.getTime(),
  //   };
  //   localStorage.setItem(key, JSON.stringify(stroageObj));
  //   console.log("stroageObj", stroageObj);
  // }
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/novel/", { state: novel.novel_id });
  };
  return (
    <div className="home-card">
      <div className="home-card-img">
        <img src={novelImg} alt="home-card-img" />
      </div>
      <div className="home-card-text">
        <div className="title" onClick={handleClick}>
          {novel.title.slice(0, 30)}
        </div>
        <div className="rating">
          <div className="stars">
            <StarRating rating={novel.rating} />
          </div>{" "}
          {novel.rating}{" "}
        </div>
        <div className="novel-chapter">
          <button className="home-card-button">
            chapter {novel.chapter_num_2}
          </button>
        </div>
        <div className="novel-chapter">
          <button className="home-card-button">
            chapter {novel.chapter_num_1}
          </button>
        </div>
      </div>
    </div>
  );
}

export default HomeCard;
