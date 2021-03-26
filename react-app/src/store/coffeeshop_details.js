const LOAD = "/shop/load";

const load = (shop) => ({
  type: LOAD,
  payload: shop
});


export const getShopAndCoffees = (shopId) => async (dispatch) => {
    const response = await fetch(`/api/shop/${shopId}/`);
    console.log("response", response)
    if (response.ok) {
        const shopAndCoffees = await response.json();
        console.log("shopAndCoffees", shopAndCoffees)
        dispatch(load(shopAndCoffees));
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