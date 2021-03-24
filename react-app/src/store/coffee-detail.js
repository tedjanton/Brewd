const LOAD = "coffee/load";

const load = (coffee) => ({
    type: LOAD,
    coffee
})

export const getCoffee = (coffeeId) => async (dispatch) => {
    const response = await fetch(`/api/coffees/${coffeeId}`)

    const coffee = await response.json();
    if (response.ok) {
        dispatch(load(coffee));
    }
    return coffee;
};

export const createSip = (sip) => async (dispatch) => {
    const {
        user_id,
        coffee_id,
        review,
        rating,
        img_src,
        created_at
    } = sip;

    const response = await fetch("/api/coffees/add-sip", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            user_id,
            coffee_id,
            review,
            rating,
            img_src,
            created_at
        })
    });

    console.log(response.json())
}

let initialState = {};

const coffeeDetailReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD: {
            newState = Object.assign({}, state);
            newState.coffee = action.coffee;
            return newState;
        }
        default:
            return state;
    }

}

export default coffeeDetailReducer;
