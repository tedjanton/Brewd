import React from "react";
import Ratings from "react-ratings-declarative";
import "./IndividualShop.css"


function IndividualShop({ shop }) {

  let ratingsSum = 0
  let allRatings = []
  if (shop?.coffees) {
    shop.coffees.forEach(coffee => {
      allRatings.push(...coffee.all_ratings);
    })
    allRatings.forEach(rating => {
      ratingsSum += rating
    })
  }

  let avg = ratingsSum/allRatings.length;

    if (shop){
        return (
             <div className="shop_content_container">
                <div className="shop_item_container">
                  <img className="shop_logo_img" src={shop.logo_src} alt=""/>
                  <div className="shop_details">
                    <p className="shop_name">
                      {shop.name}
                    </p>
                    <p className="shop_location">{`${shop.city}, ${shop.state}`}</p>
                  </div>
                </div>
                <div className="shop_spec_container">
                  <div className="shop_avg_rating">
                    <Ratings
                        rating={avg}
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
                  </div>
                  <div className="shop_total_ratings">
                    {allRatings.length} {allRatings.length === 1 ? "Review" : "Reviews"}
                  </div>
                  <div className="shop_total_coffees">{shop.coffees.length} Coffees</div>
                  <div className="shop_brewd_approved">
                    <i className="fas fa-check-circle" />
                  </div>
                </div>
                <div className="shop_description">{shop.description}</div>
              </div>
        )
    } else return (
        <>
        </>
    )
}

export default IndividualShop;
