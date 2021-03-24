import React from "react";
import "./Coffee.css";
import Ratings from "react-ratings-declarative";
import ratings from "react-ratings-declarative/build/ratings";

const Coffee = ({ coffee }) => {
  // const avg_rating = coffee.avg_rating;
  const ratings_array = coffee.all_ratings;
  console.log("all ratings", ratings_array.length);

  if (coffee) {
    return (
      <div className="main">
        <div className="box">
          <div className="content">
            <div className="coffee_item">
              <img className="coffee_pic" src={coffee.img_src} />
              <div className="coffee_details">
                <p className="coffee_name">
                  <a href="/coffees/:id">{coffee.name}</a>
                </p>
                <p className="coffee_shop">
                  <a href="/shops/:id">{coffee.shop.name}</a>
                </p>
                <p className="coffee_description">{coffee.description}</p>
              </div>
            </div>
            <div className="coffee_spec_container">
              <div className="coffee_caffeine">
                {coffee.caffeine} mg caffeine
              </div>
              <div className="coffee_type">{coffee.type}</div>
              <Ratings
                className="coffee_rating_display"
                rating={coffee.avg_rating}
                widgetDimensions="15px"
                widgetSpacings="5px"
              >
                <Ratings.Widget
                  widgetRatedColor="orange"
                  widgetEmptyColors="grey"
                />
                <Ratings.Widget
                  widgetRatedColor="orange"
                  widgetEmptyColors="grey"
                />
                <Ratings.Widget
                  widgetRatedColor="orange"
                  widgetEmptyColors="grey"
                />
                <Ratings.Widget
                  widgetRatedColor="orange"
                  widgetEmptyColors="grey"
                />
                <Ratings.Widget
                  widgetRatedColor="orange"
                  widgetEmptyColors="grey"
                />
              </Ratings>
              {/* <div className="coffee_rating_display">⭐️⭐️⭐️⭐️⭐️</div> */}
              <div className="coffee_rating_number">{coffee.avg_rating}</div>
              <div className="coffee_total_ratings">
                {coffee.all_ratings.length} Ratings
              </div>
              <div clasName="coffee_specs"></div>
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Coffee;
