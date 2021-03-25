import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addComment } from "../../store/comment";
import "./Comment.css";

const CommentForm = () => {
  const sip = useSelector((state) => state.coffeehouse.sips);
  //   console.log("SIP", sip);
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const [comment, setComment] = useState("");

  const handleSubmit = () => {
    const new_comment = {
      user_id: user.id,
      sip_id: sip.id,
      comment,
    };
    dispatch(addComment(new_comment));
  };

  return (
    <div className="comment-container">
      <textarea
        onChange={(e) => setComment(e.target.value)}
        placeholder="Leave a comment here!"
        value={comment}
      />
      <div classname="comment_button">
        <button onClick={handleSubmit}>Submit Comment</button>
      </div>
    </div>
  );
};

export default CommentForm;
