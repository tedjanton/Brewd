const GET_TOP_RATED = "/toprated/getTopRated";

const getTopRated = (coffees) => ({
  type: GET_TOP_RATED,
  payload: coffees,
});

export const topRated = () => async (dispatch) => {
  const response = await fetch("api/toprated/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const coffees = await response.json();
    dispatch(getTopRated(coffees));
    return response;
  }
};

const onlyTopRated = (coffees) => {
  let top_rated_array = [];
  let coffee_array = coffees.top_rated;
  for (let i = 0; i < coffee_array.length; i++) {
    if (coffee_array[i].avg_rating >= 3) {
      top_rated_array.push(coffee_array[i]);
    }
  }
  let new_array = top_rated_array.sort((a, b) =>
    a.avg_rating < b.avg_rating ? 1 : -1
  );
  return new_array;
};

let initialState = {};
const topRatedReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_TOP_RATED:
      const highestRated = onlyTopRated(action.payload);
      newState = Object.assign({}, state);
      newState.coffees = highestRated;
      return newState;
    default:
      return state;
  }
};

export default topRatedReducer;
