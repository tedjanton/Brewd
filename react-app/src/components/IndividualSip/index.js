import React from "react";
import "./IndividualSip.css"
import CommentForm from "../Comment/index"
import Ratings from "react-ratings-declarative";
import LikeButton from "../Like/index";
import user_icon from "../../site-images/user_icon.jpeg";


const IndividualSip = ({ sip, coffee }) => {
    
    if (sip) {
       
        return (
        <div className="sip_i">
            <div className="user_icon_i" >
                <img src={user_icon} />
            </div>
            <div className="user_input_container_i">
            <p className="text_i">
                <a className="changing_text_i">{sip.user.first_name}</a>is sipping a
                <a className="changing_text_i" href={`/coffees/${coffee.id}`}>
                {coffee.name}
                </a>
                at
                <a className="changing_text_i">{coffee.shop.name}</a>
            </p>
            <div className="review_container_i">
                <div className="inner_container_i">
                <div className="review_text_i">{sip.review}</div>
                <div className="review_middle_container_i">
                    <div className="coffee_rating_display_sip_i">
                        <Ratings
                            rating={sip.rating || 0}
                            widgetDimensions="15px"
                            widgetSpacings="5px"
                            widgetRatedColors="orange"
                            widgetEmptyColors="grey"
                        >
                            <Ratings.Widget />
                            <Ratings.Widget />
                            <Ratings.Widget />
                            <Ratings.Widget />
                            <Ratings.Widget />
                        </Ratings>
                    </div>
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
            <div className="sip_comments_container_i">
                <CommentForm sip={sip} />
            </div>
            <div className="sip_likes_container_i">
                <LikeButton sip={sip} />
            </div>
            <div className="sip_comment_responses_container_i">
                {sip.comments &&
                sip.comments.map((comment) => (
                    <div key={comment.comment.id} className="sip_comment_response_i">
                    <div>{comment.comment}</div>
                    </div>
                ))}
            </div>
            </div>
            <div className="sip_logo_container" >
            <img className="sip_logo" src={coffee.shop.logo_src} />
            </div>
        </div>
        );
    }
        else {
            return (
                <>
                </>
            )
        }
}

export default IndividualSip;
