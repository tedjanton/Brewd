import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addLike, deleteLike } from "../../store/like";

const LikeButton = ({ sip }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const userLikesArray = useSelector((state) => state.userLikes.likes)
  const [userLikeId, setUserLikeId] = useState(null);

  console.log(userLikesArray);
  useEffect(() => {
    debugger
    if (userLikesArray) {
      for (let i = 0; i < userLikesArray.length; i++) {
        let sipId = userLikesArray[i].sip_id;
        if (sipId === sip.id) {
          setUserLikeId(userLikesArray[i].id)
        } else {
          setUserLikeId(null)
        }
      }
    }
  }, [userLikesArray, setUserLikeId, sip]);


  let lk;
  if (userLikeId) {
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

    if (userLikeId) {
      // debugger
      dispatch(deleteLike(userLikeId))
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
