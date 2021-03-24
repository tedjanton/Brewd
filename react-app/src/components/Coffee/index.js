import React from "react";
import "./Coffee.css";

const Coffee = ({ coffee }) => {
  const sips = coffee?.sips;
  const rating = sips?.map((sip) => sip.rating);

  if (coffee) {
    return (
      <div className="main">
        <div className="box">
          <div className="content">
            <h3 className="top_rated_title"></h3>
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
              <div className="coffee_caffeine">{coffee.caffeine} mg</div>
              <div className="coffee_type">{coffee.type}</div>
              <div className="coffee_rating_display">⭐️⭐️⭐️⭐️⭐️</div>
              <div className="coffee_rating_number">{rating}</div>
              <div className="coffee_total_ratings">Total Ratings</div>
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
