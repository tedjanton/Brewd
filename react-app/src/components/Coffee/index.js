import React from "react";
import "./Coffee.css";

const Coffee = ({ coffee }) => {
  console.log("testing", coffee.sips);
  const sips = coffee.sips;
  const rating = sips.map((sip) => sip.rating);

  if (coffee) {
    return (
      <div className="main">
        <div className="box">
          <div className="content">
            <h3 className="top_rated_title"></h3>
            <div className="top_rated_container">
              <div className="coffee_item">{coffee.name}</div>
              <img className="coffee_pic" src={coffee.img_src} />
              <div className="coffee_details">
                <p className="coffee_name"></p>
              </div>
              <div clasName="coffee_specs"></div>
              {/* <div>About This Coffee: {coffee.description}</div>
            <div>Caffeine Content: {coffee.caffeine}mg</div>
            <div>Hot or Cold? {coffee.type}</div>
            <div>{coffee.shop.name}</div>

            <a>Rating: {rating}</a> */}
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
