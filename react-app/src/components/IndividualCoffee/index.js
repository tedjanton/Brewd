import React from "react";
import Ratings from "react-ratings-declarative";
import "./IndividualCoffee.css";

const IndividualCoffee = ({ coffee }) => {

  if (coffee) {
    return (

          <div className="content_container_i">
            <div className="coffee_item_container_i">
              <img className="coffee_pic_i" src={coffee.img_src} alt=""/>
              <div className="coffee_details_i">
                <p className="coffee_name_i">
                  {coffee.name}
                </p>
                <p className="coffee_shop_i">
                  <a href={`/shops/${coffee.shop.id}`}>{coffee.shop.name}</a>
                </p>
              </div>
            </div>
            <div className="coffee_spec_container_i">
              <div className="coffee_caffeine_i">{coffee.caffeine} mg</div>
              <div className="coffee_type_i">{coffee.type.toLowerCase()}</div>
              <div className="coffee_rating_display_container">
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
                <div className="coffee_rating_number_i">({coffee.avg_rating})</div>
              </div>
              <div className="coffee_total_ratings_i">{coffee.all_ratings.length} ratings</div>
              <div className="coffee_specs_i"></div>
            </div>
          </div>

    );
  } else {
    return <></>;
  }
};

export default IndividualCoffee;
