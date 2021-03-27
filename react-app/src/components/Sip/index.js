import React, { useEffect, useState } from "react";
import Ratings from "react-ratings-declarative";
import { Modal } from "../../context/Modal";
import CommentForm from "../Comment/index"
import LikeButton from "../Like/index";
import user_icon from "../../site-images/user_icon.png";
import "./Sip.css";
import { useSelector } from "react-redux";
import SipFormEdit from "../SipModal/SipFormEdit";

const Sip = ({ sip }) => {
  const user = useSelector(state => state.session.user)
  const [clicked, setClicked] = useState(false);
  const [showModal, setShowModal] = useState(false);

  const date = sip?.created_at.split(" ")
  const dateArr = date.splice(0, 4);
  const newDate = dateArr.join(" ");

  let commentBox;
  if (clicked) {
    commentBox = (
      <div className="sip-comment-box">
        <CommentForm
          setClicked={setClicked}
          sip={sip} />
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
        <div className="sip_comment_responses_container" key={comment.id}>
          <div className="sip_comment_response_pic">
            <img src={user_icon} alt=""/>
          </div>
          <div className="sip_comment_response_name">
            {`${comment.user.first_name} ${comment.user.last_name}:`}
          </div>
          <div  className="sip_comment_response">
            {comment.comment}
          </div>
        </div>
    );

  if (sip) {
    return (
      <div className="sip">
        <div className="user_icon" >
                <img src={user_icon} alt=""/>
            </div>
        <div className="user_input_container">
          <div className="text">
            <p className="changing_text_name">{sip.user.first_name}</p> is sipping a
            <a className="changing_text" href={`/coffees/${sip.coffee.id}`}>
              {sip.coffee.name}
            </a>
            at
            <a className="changing_text" href={`/shop/${sip.coffee.shop_id}`}>{sip.coffee.shop.name}</a>
          </div>
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
            <img className="user_uploaded_image" alt=""></img>
            <div className="sip_comment_like_container">
              <div className="sip_comment_button">
                <button onClick={() => setClicked(!clicked)}>
                  <i className="far fa-comment-alt" />Comment
                </button>
              </div>
              <LikeButton sip={sip} />
            </div>
            <div className="review_bottom_container">
              <div className="review_date">{newDate}</div>
              {(user?.id === sip.user_id) && (
                <div>
                  <button
                    onClick={() => setShowModal(true)} className="open_sip_details">Edit/Delete Sip</button>
                    {showModal && (
                      <Modal onClose={() => setShowModal(false)}>
                          <SipFormEdit
                            sip={sip}
                            coffee={sip.coffee}
                            setShowModal= {setShowModal} />
                      </Modal>
                    )}
                </div>
              )}
            </div>
            <div>
              {commentBox}
            </div>
            <div>
              {sip.comments && commentsGiven}
            </div>
          </div>
        </div>
        <div className="sip_logo_container" >
          <img className="sip_logo" src={sip.coffee.shop.logo_src} alt=""/>
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Sip;
