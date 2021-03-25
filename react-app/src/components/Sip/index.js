import React from "react";
import "./Sip.css";
import CommentForm from "../Comment/index"
import Ratings from "react-ratings-declarative";
import LikeButton from "../Like/index";
import user_icon from "../../site-images/user_icon.jpeg";

const Sip = ({ sip }) => {
  
  if (sip) {
    return (
      <div className="sip">
        <div className="user_icon" >
                <img src={user_icon} />
            </div>
        <div className="user_input_container">
          <p className="text">
            <a className="changing_text">{sip.user.first_name}</a>is sipping a
            <a className="changing_text" href={`/coffees/${sip.coffee.id}`}>
              {sip.coffee.name}
            </a>
            at
            <a className="changing_text">{sip.coffee.shop.name}</a>
          </p>
          <div className="review_container">
            <div className="inner_container">
              <div className="review_text">{sip.review}</div>
              <div className="review_middle_container">
                <Ratings
                className="coffee_rating_display_sip"
                rating={sip.coffee.avg_rating || 0}
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
                <div className="type">
                  <i className="fas fa-mug-hot icon" />
                  {sip.coffee.type}
                </div>
              </div>
            </div>
            <img className="user_uploaded_image"></img>
            <div className="review_bottom_container">
              <div className="review_date">{sip.created_at}</div>
              <div className="open_sip_details">View Sip Details</div>
            </div>
          </div>
          <div className="sip_comments_container">
            <CommentForm sip={sip} />
          </div>
          <div className="sip_likes_container">
            <LikeButton sip={sip} />
          </div>
          <div className="sip_comment_responses_container">
            {sip.comments &&
              sip.comments.map((comment) => (
                <div key={comment.comment.id} className="sip_comment_response">
                  <div>{comment.comment}</div>
                </div>
              ))}
          </div>
        </div>
        <div className="sip_logo_container" >
          <img className="sip_logo" src={sip.coffee.shop.logo_src} />
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Sip;
