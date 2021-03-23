import React from "react";
import "./Coffee.css";

const Coffee = ({ coffee }) => {
  console.log("testing", coffee.sips);
  const sips = coffee.sips;
  const rating = sips.map((sip) => sip.rating);

  if (coffee) {
    return (
      <div className="coffee">
        <div className="user_input_container">
          <p className="text">
            <a className="changing_text">{coffee.name}</a>
            <div>About This Coffee: {coffee.description}</div>
            <div>Caffeine Content: {coffee.caffeine}mg</div>
            <div>Hot or Cold? {coffee.type}</div>
            <div>{coffee.shop.name}</div>
            <img class="coffee-pics" src={coffee.img_src} />
            <a>Rating: {rating}</a>
          </p>
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Coffee;
