import React from "react";
import "./Sip.css"


const Sip = () => {
    return (
        
        <div className="sip">
                <div className="user_input_container">
                    <p className="text"><a className="changing_text" >{sip.User.first_name}</a>is sipping a <a className="changing_text">{sip.Coffee.name}</a>at<a className="changing_text">{Sip.Coffee.Shop.name}</a></p>
                    <div className="review_container">
                        <div className="inner_container">
                            <div className="review_text">{sip.review}!</div>
                            <div className="review_middle_container">
                                <div className="review_stars"></div>
                                <div className="type"> <i className="fas fa-mug-hot icon"></i>{sip.Coffee.type}</div>
                            </div>
                        </div>
                        <img className="user_uploaded_image"></img>
                        <div className="review_bottom_container">
                            <div className="review_date">{Sip.created_at}</div>
                            <div className="open_sip_details">View Sip Details</div>
                        </div>
                    </div>
                </div>
                <img className="sip_logo" src={sip.Coffee.Shop.img_src}/>
        </div>
    )
}

export default Sip;