import Header from "../components/Header";
import HomeCard from "../components/HomeCard";
import "../styles/home.css";
import History from "../components/History";
import Footer from "../components/footer";
import { baseUrl } from "../env/constant";
import { useState, useEffect } from "react";
function Home() {
  // const initialState = {
  //   novel_id: 0,
  //   title: "title",
  //   rating: 0,
  //   chapter_num_1: 1,
  //   chapter_num_2: 2,
  // };
  const [novels, setNovels] = useState([]);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    fetch(`${baseUrl}/home-cards/`, { method: "GET" })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setNovels(data);
        // console.log("data", data);
      });
  }, []);

  return (
    <>
      <Header />
      <div className="home-h1tag">
        <h2>Latest Novels</h2>
      </div>
      <div className="home-card-container">
        {novels.map((novel) => {
          return <HomeCard key={novel.novel_id} novel={novel} />;
        })}
      </div>
      <History page={true} />
      <Footer />
    </>
  );
}

export default Home;
