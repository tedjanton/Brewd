import React from "react";
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
              <div className="coffee_rating_display_i">⭐️⭐️⭐️⭐️⭐️</div>
              <div className="coffee_rating_number_i">{rating}</div>
              <div className="coffee_total_ratings_i">Total Ratings</div>
              <div clasName="coffee_specs_i"></div>
            </div>
          </div>
        
    );
  } else {
    return <></>;
  }
};

export default IndividualCoffee;
