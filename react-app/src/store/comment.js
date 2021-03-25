// const CREATE = "comment/create_comment";

// const create_comment = (comments) => ({
//   type: CREATE,
//   payload: comments,
// });

export const addComment = (new_comment) => async (dispatch) => {
  const { user_id, sip_id, comment } = new_comment;
  const response = await fetch("/api/comments/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id,
      sip_id,
      comment,
    }),
  });
  const data = await response.json();
  console.log("DATA", data);
  if (response.ok) {
    // console.log("response", response.data);
    // dispatch(create_comment(data));
    return data;
  }
};

// let initialState = {};

// const commentReducer = (state = initialState, action) => {
//   let newState;
//   switch (action.type) {
//     case CREATE: {
//       newState = Object.assign({}, state);
//       newState.comments = action.payload;
//       return newState;
//     }
//     default:
//       return state;
//   }
// };

// export default commentReducer;
