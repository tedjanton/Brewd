import React from "react";
import "./IndividualSip.css"


const IndividualSip = ({ sip, coffee }) => {

    if (sip) {
        return (
            <div className="sip">
                <div className="user_input_container">
                    <div className="text_i">
                        <a className="changing_text">{sip.user.first_name}</a>
                        is sipping a
                        <a className="changing_text">{coffee.name}</a>
                        at
                        <a className="changing_text">{coffee.shop.name}</a>
                    </div>
                    <div className="review_container">
                        <div className="inner_container">
                            <div className="review_text">
                                {sip.review}
                            </div>
                            <div className="review_middle_container">
                                <div className="review_stars"></div>
                                <div className="type">
                                    <i className="fas fa-mug-hot icon" />
                                    {coffee.type}
                                </div>
                            </div>
                        </div>
                        <img className="user_uploaded_image"></img>
                        <div className="review_bottom_container">
                            <div className="review_date">{sip.created_at}</div>
                            <div className="open_sip_details">View Sip Details</div>
                        </div>
                    </div>
                </div>
                <img className="sip_logo" src={coffee.shop.logo_src}/>
            </div>
        )

    } else {
        return (
            <>
            </>
        )
    }
}

export default IndividualSip;
