const LOAD = "/shop/load";

const load = (shop) => ({
  type: LOAD,
  payload: shop
});


export const getShop = (shopId) => async (dispatch) => {
    const response = await fetch(`/api/shop/${shopId}/`);

    if (response.ok) {
        const shop = await response.json();
        dispatch(load(shop));
        return response;
    }
};


let initialState = {};

const shopDetailReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case LOAD: {
            newState = Object.assign({}, state);
            newState.shop = action.payload;
            return newState;
        }
        default:
            return state;
    }
}

export default shopDetailReducer;
