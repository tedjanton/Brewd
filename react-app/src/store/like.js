const ADD = "/likes/add_like";
const GET_LIKES = "/likes/get_likes";
const REMOVE = "/likes/remove_like";

const add = (like) => ({
  type: ADD,
  like
})

const load = (likes) => ({
  type: GET_LIKES,
  likes
});


const remove = (like) => ({
  type: REMOVE,
  like
})

export const addLike = (newLike) => async (dispatch) => {
  const { user_id, sip_id } = newLike;
  const response = await fetch("/api/likes/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id,
      sip_id,
    }),
  });
  const addedLike = await response.json();
  if (response.ok) {
    dispatch(add(addedLike));
  }
  return addedLike;
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
  const response = await fetch(`/api/likes/${userLikeId}/delete/`);

  const deletedLike = await response.json();
  if (response.ok) {
    dispatch(remove(deletedLike))
  }
  return deletedLike;
}

let initialState = {};

const userLikesReducer = (state=initialState, action) => {
  let newState;
  switch (action.type) {
    case ADD:
      newState = Object.assign({}, state);
      if (newState.likes) {
        newState.likes = [...newState.likes, action.like]
      } else {
        newState.likes = action.like
      }
      return newState;
    case GET_LIKES:
      newState = Object.assign({}, state);
      newState.likes = action.likes.likes;
      return newState;
    case REMOVE:
      newState = Object.assign({}, state)
      newState.likes = newState.likes.filter(like => like.id !== action.like.id)
      return newState;
    default:
      return state;
  }
}

export default userLikesReducer;
