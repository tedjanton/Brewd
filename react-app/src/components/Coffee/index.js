import React from "react";
import "./Coffee.css";
import Ratings from "react-ratings-declarative";
import ratings from "react-ratings-declarative/build/ratings";

const Coffee = ({ coffee }) => {
  const sips = coffee?.sips;
  const rating = sips?.map((sip) => sip.rating);

  const ratings_array = coffee?.all_ratings;

  if (coffee) {
    return (
      <div className="main">
        <div className="box">
          <div className="content">
            <div className="coffee_item">
              <img className="coffee_pic" src={coffee.img_src} />
              <div className="coffee_details">
                <p className="coffee_name">
                  <a href={`/coffees/${coffee.id}`}>{coffee.name}</a>
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
