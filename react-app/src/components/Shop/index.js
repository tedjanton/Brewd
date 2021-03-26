import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getShop } from "../../store/coffeeshop_details";
import "./Shop.css";

const ShopDetails = () => {
    const params = useParams();
    const dispatch = useDispatch();

    const shop = useSelector((state) => {
        console.log(state.shop)
    });

    useEffect(() => {
        if (!shop) {
            dispatch(getShop(params.id))
        }
    }, [shop, dispatch])

   return (
       <>
       </>
   )
}

export default ShopDetails;