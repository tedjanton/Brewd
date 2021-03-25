import React from "react";
import Ratings from "react-ratings-declarative";
import "./IndividualCoffee.css";

const IndividualCoffee = ({ coffee }) => {
  const sips = coffee?.sips;
  const rating = sips?.map((sip) => sip.rating);

  if (coffee) {
    return (

          <div className="content_container">
            <div className="coffee_item_container">
              <img className="coffee_pic_i" src={coffee.img_src} />
              <div className="coffee_details_i">
                <p className="coffee_name_i">
                  {coffee.name}
                </p>
                <p className="coffee_shop_i">
                  <a href="/shops/:id">{coffee.shop.name}</a>
                </p>
              </div>
            </div>
            <div className="coffee_spec_container_i">
              <div className="coffee_caffeine_i">{coffee.caffeine} mg</div>
              <div className="coffee_type_i">{coffee.type}</div>
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
              <div className="coffee_rating_number_i">{rating}</div>
              <div className="coffee_total_ratings_i">Total Ratings</div>
              <div className="coffee_specs_i"></div>
            </div>
          </div>

    );
  } else {
    return <></>;
  }
};

export default IndividualCoffee;
