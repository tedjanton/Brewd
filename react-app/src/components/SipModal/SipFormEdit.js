import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import Ratings from "react-ratings-declarative";
import { editSip, deleteSip } from "../../store/coffeehouse";
import white_x from "../../site-images/white_x.png";
import add_picture from "../../site-images/add_picture.png"
import "./SipModal.css";

const SipFormEdit = ({ sip, coffee, setShowModal }) => {
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch();
    const { review, rating } = sip;
    const [newRating, setNewRating] = useState(rating ? rating : null);
    const [newReview, setNewReview] = useState(review ? review : "");
    const [newImgSrc, setNewImgSrc] = useState ("");
    const [updated, setUpdated] = useState(false);
    const [textLen, setTextLen] = useState(review.length);


    useEffect(() => {
        setTextLen(255 - newReview.length)
    }, [newReview, textLen])

    let ratingDisplay;
    if (!rating) {
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
    const updateImage = async (e) => {
        const image = e.target.files[0];
        const formData = new FormData();
        formData.append("image", image);
        const response = await fetch("/api/coffees/image/", {
            method: "POST",
            body: formData,
        });
        if (response.ok) {
            const image = await response.json();
            await setNewImgSrc(image.url)
            setUpdated(true);
        } else {
            console.log("Upload Error")
            setUpdated(false);
        }
    }

    const handleEdit = async () => {
        const submission = {
            id: sip.id,
            user_id: user.id,
            coffee_id: coffee.id,
            review: newReview,
            rating: newRating,
            img_src: newImgSrc ? newImgSrc : sip.img_src,
        }
        await dispatch(editSip(submission));
        window.location.reload();
    }

    const handleDelete = async () => {
        window.alert("Are you sure you want to delete this sip?")
        await dispatch(deleteSip(sip.id));
        window.location.reload();
    }

    return (
        <div className="sip-form-container">
            <div className="sip-form-title">
                <p>Sip Coffee</p>
                <div
                    onClick={() => setShowModal(false)}
                    className="sip-form-title-close"
                >
                    <img src={white_x} alt=""/>
                </div>
            </div>
            <div className="sip-form-review-container">
                <div className="sip-form-review-box">
                    <textarea
                        onChange={(e) => setNewReview(e.target.value)}
                        placeholder="What did you think?"
                        value={newReview}
                    />
                    <span className="sip-form-char-count">{textLen}</span>
                </div>
                <div className="sip-form-picture-container">
                    <div className="sip-form-picture">
                        <label className="sip-form-pic-upload" htmlFor="pic-upload">
                            {updated ? (
                                <i className="fas fa-check-circle" />
                                ) : (
                                <img src={add_picture} alt=""/>
                            )}
                        </label>
                        <input
                        type="file"
                        accept='image/*'
                        onChange={(e) => updateImage(e)}
                        id="pic-upload"
                        />
                    </div>
                </div>
            </div>
            <div className="sip-form-rating-container">
                <div className="sip-form-rating">
                    <Ratings
                        rating={newRating}
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
                <div className="sip-form-buttons">
                    <button onClick={handleEdit}>Edit Sip</button>
                    <button onClick={handleDelete}>Delete Sip</button>
                </div>
            </div>
        </div>
    )
}

export default SipFormEdit;
