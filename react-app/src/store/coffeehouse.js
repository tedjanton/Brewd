const LOAD = "/coffeehouse/load";
const EDIT = "sip/edit_sip";
const REMOVE = "sip/delete_sip";

const load = (sips) => ({
  type: LOAD,
  payload: sips,
});

const edit = (sip) => ({
  type: EDIT,
  sip
});

const remove = (sip) => ({
  type: REMOVE,
  sip
})

export const getSips = () => async (dispatch) => {
  const response = await fetch("/api/coffeehouse/", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    const sips = await response.json();
    dispatch(load(sips));
    return response;
  }
};

export const getUserSips = (userId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/sips/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    const userSips = await response.json();
    dispatch(load(userSips));
  }
};

export const getCoffeeSips = (coffeeId) => async (dispatch) => {
  const response = await fetch(`/api/coffees/${coffeeId}/sips/`, {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const coffeeSips = await response.json();
  if (response.ok) {
    dispatch(load(coffeeSips));
  }
  return coffeeSips;
};

export const editSip = (sip) => async (dispatch) => {
  const {
      id,
      user_id,
      coffee_id,
      review,
      rating,
      img_src
  } = sip;

  const response = await fetch(`/api/coffeehouse/edit-sip/${id}/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id,
        user_id,
        coffee_id,
        review,
        rating,
        img_src
      })
  });

  const editedSip = response.json();
  if (response.ok) {
      dispatch(edit(editedSip));
  }
  return editedSip;
};

export const deleteSip = (sipId) => async (dispatch) => {
  const response = await fetch(`/api/coffeehouse/${sipId}/delete/`)

  const deletedSip = await response.json();
  if (response.ok) {
    dispatch(remove(deletedSip));
  }
  return deletedSip;

}

const initialState = {};

const coffeehouseReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case LOAD:
      newState = Object.assign({}, state);
      newState.sips = action.payload;
      return newState;
    case EDIT:
      newState = Object.assign({}, state);
      newState.sips = [...newState, action.sip];
      return newState;
      case REMOVE:
        newState = Object.assign({}, state)
        newState.sips = newState.sips.filter(sip => sip.id !== action.sip.id)
        return newState;
    default:
      return state;
  }
};

export default coffeehouseReducer;
