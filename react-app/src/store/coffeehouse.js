const LOAD = "/coffeehouse/get_sips";

const load = (sips) => ({
  type: LOAD,
  sips,
});


export const getSips = () => async (dispatch) => {
    const response = await fetch("/api/coffeehouse/");
    if (response.ok) {
        const sips = await response.json();

        dispatch(load(sips))
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
            newState = [...state, ...action.sips]
            return newState;
        }
        default:
            return state;
    }
}

export default coffeehouseReducer;