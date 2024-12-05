import Header from "../components/Header";
import Footer from "../components/footer";
import "../styles/chapter.css";
import { IoMdArrowBack, IoMdArrowForward } from "react-icons/io";
import { TbCaretUpDownFilled } from "react-icons/tb";
import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { baseUrl } from "../env/constant";

function Chapter() {
  const [showChapterList, setShowChapterList] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();
  const chapters = location.state.chapters;
  // console.log(chapters);
  const chapter = location.state.chapter;
  const novelTitle = location.state.novelTitle;
  // console.log("chapters[0]", chapters[0].number);

  // for history store object in local storage
  function storeHistory(key, value) {
    let d = new Date();
    let stroageObj = {
      novelTitle: novelTitle,
      chapter: value,
      time: d.getTime(),
    };
    localStorage.setItem(key, JSON.stringify(stroageObj));
    // console.log("stroageObj", stroageObj);
  }
  // add views
  function addViews() {
    fetch(`${baseUrl}/novels/${chapter.novel_id}/views`, { method: "POST" });
  }
  useEffect(() => {
    storeHistory(chapter.novel_id, chapter);
    addViews();
  }, [chapter]);
  const handleClick = (chapter) => {
    storeHistory(chapter.novel_id, chapter);
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
  // chapter is getting fetched based on chapter id and not chapter number
  const getChapter = (chapter_id) => {
    fetch(`${baseUrl}/novels/chapters/${chapter_id}`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        storeHistory(chapter.novel_id, chapter);
        let history = JSON.parse(localStorage.getItem(chapter.novel_id));
        console.log("history", history);
        navigate("/chapter/", {
          state: {
            chapters: chapters,
            chapter: data,
          },
        });
        // console.log("previous chapter data", data);
      });
  };

  return (
    <>
      <Header />
      <div className="ch-container">
        {showChapterList && (
          <div className="ch-lists-upper">
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
          </div>
        )}
        <div className="ch-top-bottom-section">
          <div
            className="ch-list-selector"
            onClick={() => setShowChapterList(!showChapterList)}
          >
            chapter {chapter.number} - {chapter.title.slice(0, 60)}{" "}
            <i>
              <TbCaretUpDownFilled />
            </i>
          </div>
          <div className="ch-change-btn">
            {chapter.number > chapters[0].number && (
              <button onClick={() => getChapter(chapter.id - 1)}>
                {" "}
                <i>
                  <IoMdArrowBack />
                </i>{" "}
                Prev
              </button>
            )}
            {chapter.number < chapters[chapters.length - 1].number && (
              <button onClick={() => getChapter(chapter.id + 1)}>
                Next{" "}
                <i>
                  <IoMdArrowForward />
                </i>{" "}
              </button>
            )}
          </div>
        </div>
        <div className="ch-content">
          <p>{chapter.content}</p>
        </div>
        <div className="ch-top-bottom-section">
          <div
            className="ch-list-selector"
            onClick={() => setShowChapterList(!showChapterList)}
          >
            chapter {chapter.number} - {chapter.title.slice(0, 60)}{" "}
            <i>
              <TbCaretUpDownFilled />
            </i>
          </div>
          <div className="ch-change-btn">
            {chapter.number > chapters[0].number && (
              <button onClick={() => getChapter(chapter.id - 1)}>
                {" "}
                <i>
                  <IoMdArrowBack />
                </i>{" "}
                Prev
              </button>
            )}
            {chapter.number < chapters[chapters.length - 1].number && (
              <button onClick={() => getChapter(chapter.id + 1)}>
                Next{" "}
                <i>
                  <IoMdArrowForward />
                </i>{" "}
              </button>
            )}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}

export default Chapter;
