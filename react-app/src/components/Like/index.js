import { addLike } from "../../store/like";
import { useDispatch, useSelector } from "react-redux";
import React, { useState } from "react";

const LikeButton = ({ sip }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const likesArray = sip.likes;

  const handleSubmit = () => {
    const like = {
      user_id: user.id,
      sip_id: sip.id,
    };
    dispatch(addLike(like));
  };

  return (
    <div>
      <button onClick={handleSubmit}>Like</button>
    </div>
  );
};

export default LikeButton;
