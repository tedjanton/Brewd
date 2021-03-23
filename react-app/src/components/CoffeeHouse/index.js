import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeHouse.css";
import Sip from "../Sip";

const CoffeeHouse = ({ authenticated }) => {
    const dispatch = useDispatch();
    const sips = useSelector((state) => {
        return state.coffeehouse?.sips?.all_sips;
    });

    useEffect(() => {
        if (!sips) {
            dispatch(getSips());
        }
    }, [sips, dispatch])

     return (
        <div className="sips_container">
            <div className="page_title">Recent Global Activity</div>
                {sips?.map((sip) => (
                    <Sip sip={sip} />
                ))}
        </div>

    )

}

export default CoffeeHouse;
