import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addLike, deleteLike } from "../../store/like";

const LikeButton = ({ sip }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const likesArray = sip.likes;
  const [liked, setLiked] = useState(false)

  let userLike = [];
  useEffect(() => {
    if (likesArray.length) {
      let singleLike = likesArray.filter(like => like.user_id === user.id);
      userLike.push(singleLike)
      setLiked(true);
    }
  }, [likesArray]);

  console.log("LIKES ARRAY", likesArray)
  console.log("USERLIKE", userLike)

  let lk;
  if (liked) {
    lk = (
      <>
        <i className="fas fa-heart" />
      </>
    )
  } else {
    lk = (
      <>
        <i className="far fa-heart" />
      </>
    )
  }

  const handleSubmit = () => {
    if (liked) {
      setLiked(false)
      dispatch(deleteLike(userLike.id))

    } else {
      const like = {
        user_id: user.id,
        sip_id: sip.id,
      };
      dispatch(addLike(like));
      setLiked(true)
    }
  };

  return (
    <div>
      <div onClick={handleSubmit}>
        {lk}
      </div>
    </div>
  );
};

export default LikeButton;
