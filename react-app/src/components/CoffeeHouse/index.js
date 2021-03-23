import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeHouse.css";
import Sip from "../Sip";

const CoffeeHouse = ({ authenticated }) => {
    const dispatch = useDispatch();
    const sips = useSelector((state) => {        
        return state.coffeehouse[0];

    });

    

    const handleSips = async () => {
        const retrieveSips = await dispatch(getSips());
        return retrieveSips;
    };

    useEffect(() => {
        handleSips();
    }, []);

    if (!authenticated) {
        return <Redirect to="/" />
    }
     return (
        <div className="sips_container">
            <div className="page_title">Recent Global Activity</div>
            {sips.map((sip) => {
                <Sip />
            })}
        </div>

    )

}

export default CoffeeHouse;
