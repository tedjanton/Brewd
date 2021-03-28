import { createStore, combineReducers, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import coffeehouseReducer from "./coffeehouse";
import topRatedReducer from "./top-rated";
import featuredReducer from "./featured";
import coffeeDetailReducer from "./coffee-detail";
import userLikesReducer from "./like";
import shopDetailReducer from "./coffeeshop_details"

const rootReducer = combineReducers({
  session: sessionReducer,
  coffeehouse: coffeehouseReducer,
  topRated: topRatedReducer,
  featured: featuredReducer,
  selected: coffeeDetailReducer,
  userLikes: userLikesReducer,
  shop: shopDetailReducer,
});

let enhancer;

if (process.env.NODE_ENV === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require("redux-logger").default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
