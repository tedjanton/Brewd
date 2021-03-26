const GET_LIKES = "/likes/get_user_likes";
const REMOVE = "/likes/remove_like";

const load = (likes) => ({
  type: GET_LIKES,
  likes
});

const remove = (like) => ({
  type: REMOVE,
  like
})

export const addLike = (like) => async () => {
  const { user_id, sip_id } = like;
  const response = await fetch("/api/likes/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id,
      sip_id,
    }),
  });
  const data = await response.json();
  if (response.ok) {
    return data;
  }
};

export const getUserLikes = (userId) => async (dispatch) => {
  const response = await fetch(`/api/likes/${userId}/`)

  const likes = await response.json();
  if (response.ok) {
    dispatch(load(likes))
  }
  return likes;
}

export const deleteLike = (userLikeId) => async (dispatch) => {
  const response = await fetch(`/api/likes/${userLikeId}/delete`);

  const like = await response.json();
  if (response.ok) {
    dispatch(remove(like))
  }
  return like;
}

let initialState = {};

const userLikesReducer = (state=initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_LIKES:
      newState = Object.assign({}, state);
      newState.likes = action.likes;
      return newState;
    case REMOVE:
      return state;
    default:
      return state;
  }
}

export default userLikesReducer;
