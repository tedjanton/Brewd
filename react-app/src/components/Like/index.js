import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addLike, deleteLike } from "../../store/like";

const LikeButton = ({ sip }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const userLikesArray = useSelector((state) => state.userLikes.likes)

  const liked = !!userLikesArray.filter(like => like.sip_id === sip.id).length

  let lk;
  if (liked) {
    lk = (
      <div>
        <i className="fas fa-heart" />
      </div>
    )
  } else {
    lk = (
      <div>
        <i className="far fa-heart" />
      </div>
    )
  }

  const handleClick = async () => {
    const userLike = userLikesArray.filter(like => like.sip_id === sip.id)
    if (userLike[0]) {
      // debugger
      dispatch(deleteLike(userLike[0].id))
    } else {
      const like = {
        user_id: user.id,
        sip_id: sip.id,
      };
      dispatch(addLike(like));
    }
  };

  return (
    <div>
      <div onClick={handleClick}>
        {lk}
      </div>
    </div>
  );
};

export default LikeButton;
