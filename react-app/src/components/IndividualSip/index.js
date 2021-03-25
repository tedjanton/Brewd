import React from "react";
import "./IndividualSip.css"


const IndividualSip = ({ sip, coffee }) => {

    if (sip) {
        return (
            <div className="sip_i">
                <div className="user_input_container_i">
                    <div className="text_i">
                        <a className="changing_text_i">{sip.user.first_name}</a>
                        is sipping a
                        <a className="changing_text_i">{coffee.name}</a>
                        at
                        <a className="changing_text_i">{coffee.shop.name}</a>
                    </div>
                    <div className="review_container_i">
                        <div className="inner_container_i">
                            <div className="review_text_i">
                                {sip.review}
                            </div>
                            <div className="review_middle_container_i">
                                <div className="review_stars_i"></div>
                                <div className="type_i">
                                    <i className="fas fa-mug-hot icon_i" />
                                    {coffee.type}
                                </div>
                            </div>
                        </div>
                        <img className="user_uploaded_image_i"></img>
                        <div className="review_bottom_container_i">
                            <div className="review_date_i">{sip.created_at}</div>
                            <div className="open_sip_details_i">View Sip Details</div>
                        </div>
                    </div>
                </div>
                <div className="sip_logo_i">
                    <img src={coffee.shop.logo_src}/>
                </div>
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
