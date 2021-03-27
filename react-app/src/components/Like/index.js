import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addLike, deleteLike } from "../../store/like";

const LikeButton = ({ sip }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const userLikesArray = useSelector((state) => state.userLikes.likes)
  const [count, setCount] = useState(sip.likes.length);
  const liked = !!userLikesArray?.filter(like => like.sip_id === sip.id).length

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
      setCount(count - 1)
      dispatch(deleteLike(userLike[0].id))
    } else {
      setCount(count + 1)
      const like = {
        user_id: user.id,
        sip_id: sip.id,
      };
      dispatch(addLike(like));
    }
  };

  return (
    <div onClick={handleClick} className="sip_like_button">
      {lk}{`${count} ${count === 1 ? "Like" : "Likes"}`}
    </div>
  );
};

export default LikeButton;
