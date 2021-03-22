import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { topRated } from "../../store/top_rated";
import "./TopRated.css";

function TopRatedPage() {
  const dispatch = useDispatch();
  const { id } = useParams();
  //   const coffee = useSelector((state) => state[id]);
  //   console.log("COFFEE NAME", coffee.id);
  //   const { name, caffeine } = coffee;

  useEffect(() => {
    dispatch(topRated());
  }, [dispatch]);

  return (
    <>
      <div>
        <h1>Hi</h1>
      </div>
    </>
  );
}
export default TopRatedPage;
