import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addLike, deleteLike } from "../../store/like";

const LikeButton = ({ sip }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const userLikesArray = useSelector((state) => state.userLikes.likes)
  const sipLikes = sip.likes
  const [liked, setLiked] = useState()

  useEffect(() => {
    getUserLike();
  });

  useEffect(() => {
    let checked = getUserLike();
    if (checked) {
      setLiked(true)
    } else {
      setLiked(false)
    }
  }, [userLikesArray])

  const getUserLike = () => {
    if (userLikesArray) {
      for (let i = 0; i < userLikesArray.length; i++) {
        let sipId = userLikesArray[i].sip_id;
        if (sipId === sip.id) {
          setLiked(true);
          return userLikesArray[i];
        } else {
          setLiked(false);
          return null;
        }
      }
    }
  }

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
    let userLike = getUserLike();

    if (liked) {
      dispatch(deleteLike(userLike.id))
      setLiked(false)
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
      <div onClick={handleClick}>
        {lk}
      </div>
    </div>
  );
};

export default LikeButton;
