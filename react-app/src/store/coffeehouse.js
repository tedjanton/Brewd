const LOAD = "/coffeehouse/load";

const load = (sips) => ({
  type: LOAD,
  payload: sips,
});


export const getSips = () => async (dispatch) => {
    const response = await fetch("/api/coffeehouse/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    console.log(response)
    if (response.ok) {
        const sips = await response.json();
        dispatch(load(sips))
        return response;
    }
}

export const getUserSips = (userId) => async (dispatch) => {
    const response = await fetch(`/api/users/${userId}/sips`)
     
            const userSips = await response.json();
            console.log("=======>", userSips)
            dispatch(load(userSips))
   
}

const initialState = [];

const coffeehouseReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD: {
            newState = [...state, action.payload]
            return newState;
        }
        default:
            return state;
    }
    
}

export default coffeehouseReducer;