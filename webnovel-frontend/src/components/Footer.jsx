import "../styles/footer.css";
import { Link } from "react-router-dom";

function footer() {
  return (
    <>
      <div className="footer">
        <div className="footer-top">
          <div className="footer-top-text">
            <p className="footer-text">
              <Link to="/">Home</Link>
            </p>
            <p>|</p>
            <p className="footer-text">Contact Us</p>
            <p>|</p>
            <p className="footer-text">Privacy</p>
          </div>
        </div>
        <div className="footer-bottom">
          <div className="footer-bottom-text">
            <p>© 2023 WebNovel All Rights Reserved</p>
          </div>
        </div>
      </div>
    </>
  );
}

export default footer;
