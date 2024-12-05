import "../styles/ChapterList.css";
import { FaStar } from "react-icons/fa";
import { FaCaretRight } from "react-icons/fa";
import { HiMiniArrowsUpDown } from "react-icons/hi2";
import { useState } from "react";
import { TbTriangleInvertedFilled, TbTriangleFilled } from "react-icons/tb";
import { useNavigate } from "react-router-dom";
function ChapterList({ chapters, novelTitle }) {
  const [showMoreChapter, setShowMoreChapter] = useState(false);
  const navigate = useNavigate();
  // function storeHistory(key, value) {
  //   let d = new Date();
  //   let stroageObj = {
  //     novelTitle: novelTitle,
  //     chapter: value,
  //     time: d.getTime(),
  //   };
  //   localStorage.setItem(key, JSON.stringify(stroageObj));
  //   console.log("stroageObj", stroageObj);
  // }
  const handleClick = (chapter) => {
    // storeHistory(chapter.novel_id, chapter);
    // let history = JSON.parse(localStorage.getItem(chapter.novel_id));
    // console.log("history", history);
    navigate("/chapter/", {
      state: {
        chapters: chapters,
        chapter: chapter,
        novelTitle: novelTitle,
      },
    });
  };
  const ToggleChapter = () => {
    setShowMoreChapter(!showMoreChapter);
  };

  return (
    <>
      <div className="ch-list-title">
        <div className="star">
          <i className="star-icon">
            <FaStar />
          </i>{" "}
          <i>
            <FaCaretRight />
          </i>
        </div>
        <span className="ch-bold-text"> LATEST CHAPTER RELEASES</span>
        <i className="arrows">
          <HiMiniArrowsUpDown />
        </i>
      </div>
      {chapters.map((chapter) => {
        return (
          <div
            className="chapter-list"
            key={chapter.id}
            onClick={handleClick.bind(this, chapter)}
          >
            <div className="ch-title">
              {chapter.number} - {chapter.title}
            </div>
            <div className="time"> 4 Hours ago</div>
          </div>
        );
      })}
      <div className="show-more">
        <div className="show-more-text" onClick={ToggleChapter}>
          {showMoreChapter ? "Show Less" : "Show More"}

          <i>
            {showMoreChapter ? (
              <TbTriangleFilled size={12} />
            ) : (
              <TbTriangleInvertedFilled size={12} />
            )}
          </i>
        </div>
      </div>
    </>
  );
}

export default ChapterList;
