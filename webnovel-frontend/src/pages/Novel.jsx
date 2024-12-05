import Header from "../components/Header";
import NovelCard from "../components/NovelCard";
import "../styles/novel.css";
import Summary from "../components/Summary";
import History from "../components/History";
import ChapterList from "../components/ChapterList";
import Footer from "../components/footer";
import { useLocation } from "react-router-dom";
import { useState, useEffect } from "react";
import { baseUrl } from "../env/constant";
function Novel() {
  const location = useLocation();
  const novel_id = location.state;
  // console.log("novel_id", novel_id);

  const [novel, setNovel] = useState({});
  const [rating, setRating] = useState({});
  const [rank, setRank] = useState(0);
  const [views, setViews] = useState(0);
  const [genres, setGenres] = useState([]);
  const [chapters, setChapters] = useState([]);

  useEffect(() => {
    getNovel();
    getRating();
    getRank();
    getViews();
    getGenres();
    getChapters();
  }, []);
  function getNovel() {
    fetch(`${baseUrl}/novels/${novel_id}`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setNovel(data);
        // console.log("novel data", data);
      });
  }
  function getRating() {
    fetch(`${baseUrl}/novels/${novel_id}/ratings`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setRating(data);
        // console.log("rating data", data);
      });
  }
  function getRank() {
    fetch(`${baseUrl}/novels/${novel_id}/rank`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setRank(data.rank);
        // console.log("rank data", data.rank);
      });
  }
  function getViews() {
    fetch(`${baseUrl}/novels/${novel_id}/views`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setViews(data);
        // console.log("views data", data);
      });
  }
  function getGenres() {
    fetch(`${baseUrl}/novels/${novel_id}/genres`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        data.map((genre) => {
          setGenres((prev) => [...prev, genre.name, ", "]);
        });
        // console.log("genres data", data);
      });
  }
  function getChapters() {
    fetch(`${baseUrl}/novels/${novel_id}/chapters`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setChapters(data);
        // console.log("chapters data", data);
      });
  }
  return (
    <>
      <Header />
      <div className="novel-title">{novel.title}</div>
      <NovelCard
        novel_id={novel_id}
        author={novel.author}
        rating={rating}
        rank={rank}
        views={views}
        genres={genres}
        chapters={chapters}
      />
      <div className="summary-container">
        <Summary summary={novel.description} />
        <History />
      </div>
      <div className="chapter-list-container">
        <ChapterList chapters={chapters} novelTitle={novel.title} />
      </div>
      <Footer />
    </>
  );
}

export default Novel;
