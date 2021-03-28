import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getShop } from "../../store/coffeeshop_details";
import IndividualShop from "../IndividualShop";
import Coffee from "../Coffee";
import "./Shop.css";

const ShopDetails = () => {
    const params = useParams();
    const dispatch = useDispatch();

    const shop = useSelector((state) => {
        return state.shop?.shop?.individual_shop
    });

    useEffect(() => {
        dispatch(getShop(params.id))
    }, [params, dispatch])

   return (
       <>
            <div className="shop_details_page_container">
                <div className="shop_details_page_container_top">
                    <div className="individual_shop_container">
                        <IndividualShop shop={shop} />
                    </div>
                </div>
                <div className="shop_coffees_container">
                    {shop?.coffees?.map(coffee => (
                        <Coffee key={coffee.id} coffee={coffee} shop={shop}/>
                    ))}
                </div>
            </div>
       </>
   )
}

export default ShopDetails;
