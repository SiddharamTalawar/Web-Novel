import { FaStar } from "react-icons/fa";
import { useState, useEffect } from "react";
function StarRating({ rating }) {
  const [rate, setRate] = useState(0);

  useEffect(() => {
    setRate(rating);
  }, [rating]);

  return (
    <>
      {[...Array(5)].map((star, index) => {
        const getIndex = index + 1;
        return (
          <div key={index}>
            <label>
              <input
                type="radio"
                name="rating"
                value={getIndex}
                onClick={() => setRate(getIndex)}
              />
              <FaStar
                className="star"
                color={getIndex <= rate ? "#ffc107" : "#c3c5c7"}
              />
            </label>{" "}
          </div>
        );
      })}
    </>
  );
}

export default StarRating;
