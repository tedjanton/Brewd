import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom";
import { getFeaturedCoffees } from "../../store/featured"
import "./Featured.css"

const Featured = () => {
    const dispatch = useDispatch()
    const coffees = useSelector((state) => state.featured?.coffees?.featured_coffees);

    useEffect(() => {
        if (!coffees) {
            dispatch(getFeaturedCoffees());
        }
    }, [coffees, dispatch])

    return (
        <div className ="featured_container">
            <div className="featured_title">Featured Coffees</div>
            {coffees?.map((coffee) => (
                <div key={coffee.id} className="featured_coffee">
                    <img className="featured_coffee_img" src={coffee.img_src}/>
                    <div className="featured_text_container">
                        <Link to={`/coffees/${coffee.id}`} className="featured_coffee_name">{coffee.name}</Link>
                        <p className="featured_coffee_shop">{coffee.shop.name}</p>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default Featured;
