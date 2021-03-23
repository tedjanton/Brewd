import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeHouse.css";

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
            <div className="sip">
                <div className="user_input_container">
                    <p className="text"><a className="changing_text" >Demo</a>is sipping a <a className="changing_text">Malt Ball Latte</a>at<a className="changing_text">ReAnimator Coffee</a></p>
                    <div className="review_container">
                        <div className="inner_container">
                            <div className="review_text">super tasty and unique!</div>
                            <div className="review_middle_container">
                                <div className="review_stars"></div>
                                <div className="type"> <i className="fas fa-mug-hot icon"></i>hot</div>
                            </div>
                        </div>
                        <img className="user_image"></img>
                        <div className="review_bottom_container">
                            <div className="review_date">7/12/2020</div>
                            <div className="open_sip_details">View Sip Details</div>
                        </div>
                    </div>
                </div>
                <img className="sip_logo" src="https://pbs.twimg.com/profile_images/833752955862052868/f59GA6nj_400x400.jpg"/>

            </div>
        </div>

    )

}

export default CoffeeHouse;
