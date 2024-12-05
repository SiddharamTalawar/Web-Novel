import { Routes, Route, BrowserRouter } from "react-router-dom";
import Home from "./pages/Home";
import Novel from "./pages/Novel";
import Chapter from "./pages/Chapter";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/novel/" element={<Novel />} />
          <Route path="/chapter/" element={<Chapter />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
