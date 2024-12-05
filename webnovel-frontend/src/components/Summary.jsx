import { FaStar } from "react-icons/fa";
import "../styles/summary.css";
import { FaCaretRight } from "react-icons/fa";
import { TbTriangleInvertedFilled, TbTriangleFilled } from "react-icons/tb";
import { useState } from "react";
function Summary({ summary }) {
  const [showMoreSummary, setShowMoreSummary] = useState(false);
  const [animationActive, setAnimationActive] = useState(false);
  const ToggleSummary = () => {
    setShowMoreSummary(!showMoreSummary);
    setAnimationActive(!animationActive);
  };
  const onAnimationEnd = () => {
    setAnimationActive(false);
  };

  return (
    <div className="summary">
      <div className="summary-title">
        <div className="">
          <i className="star-icon">
            <FaStar />
          </i>{" "}
          <i>
            <FaCaretRight />
          </i>
        </div>
        <span className="summary-bold-text">Summary</span>
      </div>
      <div className="summary-detail-container">
        <p className="summary-bold-text">Synopsis</p>
        {showMoreSummary ? <p className="summary-detail">{summary}</p> : null}
        <div className="show-more">
          <div
            className={"show-more-text" + (animationActive ? " animate" : "")}
            onClick={ToggleSummary}
            onAnimationEnd={onAnimationEnd}
          >
            {showMoreSummary ? "Show Less" : "Show More"}

            <i>
              {showMoreSummary ? (
                <TbTriangleFilled size={12} />
              ) : (
                <TbTriangleInvertedFilled size={12} />
              )}
            </i>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Summary;
