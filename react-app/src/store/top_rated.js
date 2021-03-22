const GET_TOP_RATED = "/top_rated/getTopRated";

const getTopRated = (sip) => ({
  type: GET_TOP_RATED,
  payload: sip,
});

export const topRated = () => async (dispatch) => {
  const response = await fetch("api/top_rated/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
    console.log("hi!!!!", data);
    dispatch(getTopRated(data));
    return response;
  }
};

let initialState = {};
const topRatedReducer = (state = initialState, action) => {
  const newState = Object.assign({}, state);
  switch (action.type) {
    case GET_TOP_RATED:
      console.log("PAYLOAD", action.payload);
      //   for (let sip of action.payload) {
      //     newState[sip.id] = sip;
      //   }
      newState[action.payload.id] = action.payload;
      console.log("NEW STATE", newState);
      return newState;
    default:
      return state;
  }
};

export default topRatedReducer;
