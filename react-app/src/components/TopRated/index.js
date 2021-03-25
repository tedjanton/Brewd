import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { topRated } from "../../store/top_rated";
import "./TopRated.css";
import Coffee from "../Coffee";
import Featured from "../Featured";

function TopRatedPage() {
  const dispatch = useDispatch();
  const coffees = useSelector((state) => {
    return state.topRated?.coffees?.top_rated;
  });
  console.log("THIS IS IT", coffees);

  //   const { id } = useParams();
  //   const coffee = useSelector((state) => {
  //     return state.topRated[0];
  //   });
  //   console.log("COFFEE NAME", coffee.id);
  //   const { name, caffeine } = coffee;

  useEffect(() => {
    if (!coffees) {
      dispatch(topRated());
    }
  }, [coffees, dispatch]);

  return (
    <>
    {/* added className and some css */}
      <div className="topRated">
        <div className="top_rated_container">
          <h1 className="top_rated_title">Top Rated Coffees</h1>
          {coffees?.map((coffee) => (
            <Coffee coffee={coffee} />
          ))}
        </div>
        <Featured />
      </div>
    </>
  );
}
export default TopRatedPage;
