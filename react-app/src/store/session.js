const GET_USER = "/session/get_user";
const CREATE_USER = "/session/create_user";

const getUser = (user) => ({
  type: GET_USER,
  user,
});

const createUser = (user) => ({
  type: CREATE_USER,
  user,
});

export const authenticate = async () => {
  const response = await fetch("/api/auth/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  return await response.json();
};

export const login = (email, password) => async (dispatch) => {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });

  if (response.ok) {
    let data = await response.json();
    dispatch(getUser(data));
    return response;
  }
};

export const logout = async () => {
  const response = await fetch("/api/auth/logout", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  return await response.json();
};

export const signUp = (
  username,
  first_name,
  last_name,
  email,
  password
) => async (dispatch) => {
  const response = await fetch("/api/auth/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      first_name,
      last_name,
      email,
      password,
    }),
  });
  if (response.ok) {
    let data = await response.json();
    dispatch(createUser(data));
    return response;
  }
};

let initialState = { user: null };

const sessionReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_USER:
      newState = Object.assign({}, state);
      // console.log(action)
      newState.user = action.user;
      return newState;
    case CREATE_USER:
      newState = Object.assign({}, state);
      newState.user = action.user;
      return newState;
    // console.log(action.user)
    default:
      return state;
  }
};

export default sessionReducer;
