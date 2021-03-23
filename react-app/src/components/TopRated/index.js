import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { topRated } from "../../store/top_rated";
import "./TopRated.css";
import Coffee from "../Coffee";

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
      <div>
        <h1>Top Rated Coffees</h1>
        {coffees?.map((coffee) => (
          <Coffee coffee={coffee} />
        ))}
      </div>
    </>
  );
}
export default TopRatedPage;
