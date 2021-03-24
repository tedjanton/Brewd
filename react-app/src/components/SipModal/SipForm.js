import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import Ratings from "react-ratings-declarative";
import { useHistory } from "react-router";
import { createSip } from "../../store/coffee-detail";
import "./SipModal.css";

const SipForm = () => {
    const coffee = useSelector(state => state.selected.coffee)
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch();
    const history = useHistory();
    const [rating, setRating] = useState(0);
    const [review, setReview] = useState("");

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
                <p className="rating-top">{rating}</p>
                <p className="rating-bottom">STARS</p>
            </>
        )
    }

    const handleSubmit = () => {
        const submission = {
            user_id: user.id,
            coffee_id: coffee.id,
            review,
            rating,
            img_src: "",
        }
        console.log(submission)
        dispatch(createSip(submission))
        // return history.push("/home")
    }

    return (
        <div className="sip-form-container">
            <div className="sip-form-title">
                <p>Sip Coffee</p>
            </div>
            <div className="sip-form-review-box">
                <textarea
                    onChange={(e) => setReview(e.target.value)}
                    placeholder="What did you think?"
                    value={review}
                />
                <span className="sip-form-char-count">255</span>
            </div>
            <div className="sip-form-picture-container">
                <div className="sip-form-picture">
                    <i className="fas fa-camera" />
                </div>
            </div>
            <div className="sip-form-rating-container">
                <div className="sip-form-rating">
                    <Ratings
                        rating={rating}
                        changeRating={setRating}
                        widgetRatedColor="yellow"
                        widgetRatedColors="#ffc935"
                        widgetEmptyColors="#dfdfdf"
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
                    {ratingDisplay}
                </div>
                <div className="sip-form-facebook-icon">
                    <i className="fab fa-facebook-square" />
                </div>
                <div className="sip-form-location-container">
                    <div>{coffee.shop.name} in {coffee.shop.city}</div>
                </div>
                <div className="sip-form-button">
                    <button onClick={handleSubmit}>Confirm</button>
                </div>
            </div>
        </div>
    )
}

export default SipForm;
