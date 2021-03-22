const LOAD = "/coffeehouse/get_sips";

const load = (sips) => ({
  type: LOAD,
  payload: sips,
});


export const getSips = () => async (dispatch) => {
    const response = await fetch("/api/coffeehouse/");
    if (response.ok) {
        const sips = await response.json();

        dispatch(load(sips))
    }
}

const initialState = [];

const coffeehouseReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD: {
            newState = [...state, ...action.payload]
            return newState;
        }
        default:
            return state;
    }
}

export default coffeehouseReducer;