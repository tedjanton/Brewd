import React from "react";
import "./Coffee.css";
import Ratings from "react-ratings-declarative";

const Coffee = ({ coffee, shop }) => {

  if (coffee) {
    return (
      <div className="main">
        <div className="box">
          <div className="content">
            <div className="coffee_item">
              <img className="coffee_pic" src={coffee.img_src} alt=""/>
              <div className="coffee_details">
                <p className="coffee_name">
                  <a href={`/coffees/${coffee.id}`}>{coffee.name}</a>
                </p>
                <p className="coffee_shop">
                  <a href={`/shops/${coffee.shop ? coffee.shop.id : ""}`}>{coffee.shop ? coffee.shop.name : shop.name}</a>
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
                widgetRatedColors="orange"
                widgetEmptyColors="grey"
              >
                <Ratings.Widget />
                <Ratings.Widget />
                <Ratings.Widget />
                <Ratings.Widget />
                <Ratings.Widget />
              </Ratings>
              <div className="coffee_rating_number">{coffee.avg_rating}</div>
              <div className="coffee_total_ratings">
                {coffee.all_ratings.length} {
                coffee.all_ratings.length === 1 ? "Rating" : "Ratings"
                }
              </div>
              <div className="coffee_specs"></div>
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
