import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeHouse.css";

const CoffeeHouse = ({ authenticated }) => {
    const dispatch = useDispatch();
    const sips = useSelector((state) => {
        
        return state.coffeehouse[0]
    });

        console.log("SIPS", sips)

    const handleSips = async () => {
        const retrieveSips = await dispatch(getSips());
        return retrieveSips;
    };
    
    useEffect(() => {
        handleSips();
    }, []);
    
    if (!authenticated) {
        return <Redirect to="/" />}
     return (
        <div className="sips_container">
            <h2>Recent Global Activity</h2>
            <div className="sip">
                <div className="">
                    <div className="text_container">
                        <p className="changing_text">Demo</p>
                        <p>is sipping a</p>
                        <p className="changing_text">Malt Ball Latte</p>
                        <p>at</p>
                        <p className="changing_text">ReAnimator Coffee</p>
                    </div>
                </div>
                <img className="sip_logo" src="https://pbs.twimg.com/profile_images/833752955862052868/f59GA6nj_400x400.jpg"/>
                    
            </div>
        </div>

    )
    
}

export default CoffeeHouse;