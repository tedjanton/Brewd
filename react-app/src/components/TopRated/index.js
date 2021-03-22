import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { topRated } from "../../store/top_rated";
import "./TopRated.css";

function TopRatedPage() {
  const dispatch = useDispatch();
  //   const coffee = useSelector((state) => state.coffee.name);
  useEffect(() => {
    dispatch(topRated());
  }, [dispatch]);

  return (
    <>
      <div>
        <h1></h1>
      </div>
    </>
  );
}
export default TopRatedPage;
