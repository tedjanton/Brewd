import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeHouse.css";

const CoffeeHouse = ({ authenticated }) => {
    const dispatch = useDispatch();
    const sips = useSelector((state) => {
        console.log("STATE", state);
        return state.coffeeHouse
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
    } return (
        <>
            <h2>Hello From Coffee House</h2>
            <div>
                {sips.map((sip) => {
                    <div className="sip" key={sip.id}>
                    </div>
                })}
            </div>
        </>

    )
    
}

export default CoffeeHouse;