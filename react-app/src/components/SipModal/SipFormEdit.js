import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import Ratings from "react-ratings-declarative";
import { useHistory } from "react-router";
import { createSip } from "../../store/coffee-detail";
import white_x from "../../site-images/white_x.png";
import add_picture from "../../site-images/add_picture.png"
import "./SipModal.css";

const SipFormEdit = ({ sip, coffee, setShowModal }) => {
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch();
    const history = useHistory();
    const [newRating, setNewRating] = useState(0);
    const [newReview, setNewReview] = useState("");
    const [textLen, setTextLen] = useState(0);

    const {
        user_id,
        coffee_id,
        review,
        rating,
        img_src
    } = sip;

    useEffect(() => {
        setTextLen(255 - newReview.length)
    }, [newReview, textLen])

    let ratingDisplay;
    if (rating === 0) {
        ratingDisplay = (
            <>
                <p className="rating-top">NO</p>
                <p className="rating-bottom">RATING</p>
            </>
        )
    } else {
        ratingDisplay = (
            <>
                <p className="rating-top">{newRating}</p>
                <p className="rating-bottom">STARS</p>
            </>
        )
    }

    const handleSubmit = () => {
        const submission = {
            user_id: user.id,
            coffee_id: coffee.id,
            review: newReview,
            rating: newRating,
            img_src: "",
        }
        dispatch(createSip(submission))
        return history.push("/home")
    }

    const handleDelete = () => {
        
    }

    return (
        <div className="sip-form-container">
            <div className="sip-form-title">
                <p>Sip Coffee</p>
                <div
                    onClick={() => setShowModal(false)}
                    className="sip-form-title-close"
                >
                    <img src={white_x}/>
                </div>
            </div>
            <div className="sip-form-review-container">
                <div className="sip-form-review-box">
                    <textarea
                        onChange={(e) => setNewReview(e.target.value)}
                        placeholder="What did you think?"
                        value={newReview || review}
                    />
                    <span className="sip-form-char-count">{textLen}</span>
                </div>
                <div className="sip-form-picture-container">
                    <div className="sip-form-picture">
                        <img src={add_picture}/>
                    </div>
                </div>
            </div>
            <div className="sip-form-rating-container">
                <div className="sip-form-rating">
                    <Ratings
                        rating={newRating || rating}
                        changeRating={setNewRating}
                        widgetRatedColors="#ffc935"
                        widgetEmptyColors="#8f8f8f"
                        widgetHoverColors="#ffc935"
                        widgetDimensions="36px"
                    >
                        <Ratings.Widget />
                        <Ratings.Widget />
                        <Ratings.Widget />
                        <Ratings.Widget />
                        <Ratings.Widget />
                    </Ratings>
                </div>
                <div className="sip-form-rating-display">
                    <i className="fas fa-caret-left" />
                    {ratingDisplay}
                </div>
                <div className="sip-form-rating-divider"></div>
                <div className="sip-form-facebook-icon">
                    <i className="fab fa-facebook-square" />
                </div>
            </div>
            <div className="sip-form-location-button-container">
                <div className="sip-form-location-container">
                    <i className="fas fa-map-marker-alt" />
                    <div className="sip-form-location">{coffee?.shop?.name} in {coffee?.shop?.city}</div>
                </div>
                <div className="sip-form-button">
                    <button onClick={handleSubmit}>Edit Sip</button>
                    <button onClick={handleDelete}>Delete Sip</button>
                </div>
            </div>
        </div>
    )
}

export default SipFormEdit;
