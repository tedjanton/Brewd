import React, { useEffect, useState } from "react";
import Ratings from "react-ratings-declarative";
import { Link } from "react-router-dom";
import { Modal } from "../../context/Modal";
import SipForm from "../SipModal/SipForm";
import CommentForm from "../Comment/index"
import LikeButton from "../Like/index";
import user_icon from "../../site-images/user_icon.jpeg";
import "./Sip.css";
import { useSelector } from "react-redux";
import SipFormEdit from "../SipModal/SipFormEdit";

const Sip = ({ sip }) => {
  const user = useSelector(state => state.session.user)
  const [clicked, setClicked] = useState(false);
  const [showModal, setShowModal] = useState(false);

  let commentBox;
  if (clicked) {
    commentBox = (
      <div className="sip-comment-box">
        <CommentForm setClicked={setClicked} sip={sip} />
      </div>
    )
  } else {
    commentBox = (
      <>
      </>
    )
  }

  useEffect(() => {

  }, [sip])


  const commentsGiven = sip.comments
    .sort((a, b) => a.id < b.id ? 1 : -1)
    .map((comment) =>
        <div key={comment.id} className="sip_comment_response">
          {comment.comment}
        </div>
    );

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
            <a className="changing_text" href={`/shop/${sip.coffee.shop_id}`}>{sip.coffee.shop.name}</a>
          </p>
          <div className="review_container">
            <div className="inner_container">
              <div className="review_text">{sip.review}</div>
              <div className="review_middle_container">
                <div className="coffee_rating_display_sip">
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
                <div className="type">
                  <i className="fas fa-mug-hot icon" />
                  {sip.coffee.type}
                </div>
              </div>
            </div>
            <img className="user_uploaded_image"></img>
            <div className="review_bottom_container">
              <div className="review_date">{sip.created_at}</div>
              {(user.id === sip.user_id) && (
                <div>
                  <button
                    onClick={() => setShowModal(true)} className="open_sip_details">Edit/Delete Sip</button>
                    {showModal && (
                      <Modal onClose={() => setShowModal(false)}>
                          <SipFormEdit
                            sip={sip}
                            coffee={sip.coffee}
                            setShowModal= {setShowModal}/ >
                      </Modal>
                    )}
                </div>
              )}
            </div>
          </div>
          <div className="sip_comment_like_container">
            <div className="sip_comment_button">
              <button onClick={() => setClicked(true)}>Comment</button>
              {commentBox}
            </div>
            <div className="sip_like_button">
              <LikeButton sip={sip} />
            </div>
            <div className="sip_comment_responses_container">
              {commentsGiven}
            </div>
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
