import "../styles/history.css";
import { TbTriangleInvertedFilled } from "react-icons/tb";
import { useNavigate } from "react-router-dom";
function History({ page }) {
  // const navigate = useNavigate();
  // const historyHandleClick = () => {
  //   navigate("/chapter/", {
  //     state: {
  //       chapters: chapters,
  //       chapter: chapter,
  //       novelTitle: novelTitle,
  //     },
  //   });
  // }
  const items = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    const value = JSON.parse(localStorage.getItem(key));
    items.push({ key, value });
  }
  items.sort((a, b) => b.value.time - a.value.time); // sort by time in descending order

  return (
    <div className="history">
      <div className="history-text">
        My Reading History{" "}
        <i className="down-triangle">
          <TbTriangleInvertedFilled size={25} />
        </i>
      </div>
      <div className="history-novels">
        {items.slice(0, 6).map((item) => (
          <p
            className={page ? "history-novel-title" : "history-chapter-title"}
            key={item.key}
          >
            {item.value.novelTitle}
          </p>
        ))}
      </div>
    </div>
  );
}

export default History;
