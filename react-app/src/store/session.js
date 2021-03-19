const SET_USER = "session/SET_USER";

const setUser = (user) => ({
    type: SET_USER,
    user
})

export const getUser = (user) => async dispatch => {
    const { email, password } = user;

    const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    if (res.ok) {
        const data = await res.json()
        dispatch(setUser(data.user))
        return res;
    }
}

const initialState = { user: null }

const sessionReducer = (state = initialState, action) => {
    let newState;
    switch (action.type) {
        case SET_USER:
            newState = Object.assign({}, state)
            newState.user = action.user
            return newState;
        default:
            return state;
    }
}

export default sessionReducer;
