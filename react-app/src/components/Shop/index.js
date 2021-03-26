import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import coffeehouseReducer from "../../store/coffeehouse";
import { getShopAndCoffees } from "../../store/coffeeshop_details";
import "./Shop.css";

const ShopDetails = () => {
    const params = useParams();
    const dispatch = useDispatch();

    const shop = useSelector((state) => {
        console.log(state.shop)
    });

    const coffees = useSelector((state) => {
        return state.shop?.shop?.coffees_by_shop
    })

    useEffect(() => {
        if (!shop || !coffees ) {
            dispatch(getShopAndCoffees(params.id))
        }
    }, [shop, coffees, dispatch])

   return (
       <>
       </>
   )
}

export default ShopDetails;