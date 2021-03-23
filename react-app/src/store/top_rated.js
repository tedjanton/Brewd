const GET_TOP_RATED = "/top_rated/getTopRated";

const getTopRated = (coffees) => ({
  type: GET_TOP_RATED,
  payload: coffees,
});

export const topRated = () => async (dispatch) => {
  const response = await fetch("api/top_rated/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const coffees = await response.json();
    console.log("hi!!!!", coffees);
    dispatch(getTopRated(coffees));
    return response;
  }
};

let initialState = {};
const topRatedReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_TOP_RATED:
      //   console.log("PAYLOAD", action.payload);
      newState = Object.assign({}, state);
      newState.coffees = action.payload;
      //   console.log("NEW STATE", newState);
      return newState;
    default:
      return state;
  }
};

export default topRatedReducer;
