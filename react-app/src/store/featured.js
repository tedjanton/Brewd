const LOAD = "/featured/load";

const load = (coffee) => ({
    type: LOAD,
    payload: coffee,
});


export const getFeaturedCoffees = () => async (dispatch) => {
    const response = await fetch("/api/featured/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    if (response.ok) {
        const coffees = await response.json();
        dispatch(load(coffees))
        return response;
    }
};

const initialState = {};

const featuredReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD: {
            newState = Object.assign({}, state);
            newState.coffees = action.payload;
            return newState;
        }
        default:
            return state;
    }
}

export default featuredReducer;