import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { topRated } from "../../store/top-rated";
import "./TopRated.css";
import Coffee from "../Coffee";
import Featured from "../Featured";

function TopRatedPage() {
  const dispatch = useDispatch();
  const coffees = useSelector((state) => {
    return state.topRated?.coffees;
  });

  useEffect(() => {
    if (!coffees) {
      dispatch(topRated());
    }
  }, [coffees, dispatch]);

  return (
    <>
      <div className="top_rated_page_container">
        <div className="top_rated_container">
          <h1 className="top_rated_title">Top Rated Coffees</h1>
          <h2 className="top_rated_blurb">
            This list shows the top coffees based on the average user ratings.
            Have fun exploring, and be sure to rate your favorite coffees!
          </h2>
          {coffees?.map((coffee) => (
            <Coffee key={coffee.id} coffee={coffee} />
          ))}
        </div>
        <Featured />
      </div>
    </>
  );
}
export default TopRatedPage;
