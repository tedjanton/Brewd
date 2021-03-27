import React from "react";
import "./IndividualShop.css"

function IndividualShop({ shop }) {
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
                    {/* <Ratings
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
                    </Ratings> */}
                  </div>
                  <div className="shop_total_ratings"></div>
                  <div className="shop_total_coffees">{shop.coffees.length} Coffees</div>
                  <div className="shop_brewd_approved"></div>
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
