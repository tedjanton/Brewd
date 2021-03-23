const LOAD = "/sips/load";

const load = (sips) => ({
  type: LOAD,
  payload: sips,
});


export const getSips = () => async (dispatch) => {
    const response = await fetch("/api/sips/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    if (response.ok) {
        const sips = await response.json();
        dispatch(load(sips))
        return response;
    }
}

export const getUserSips = (userId) => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}/sips`, {
        headers: {
            "Content-Type": "application/json",
        }
    });

    if (response.ok) {
        const userSips = await response.json();
        dispatch(load(userSips))
        return response;
    }
}

const initialState = {};

const sipsReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD: {
            newState = Object.assign({}, state);
            newState.sips = action.payload;
            return newState;
        }
        default:
            return state;
    }

}

export default sipsReducer;
