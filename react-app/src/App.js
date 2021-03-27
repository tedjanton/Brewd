import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import Landing from "./components/Landing";
import CoffeeHouse from "./components/CoffeeHouse";
import { authenticate } from "./store/session";
import TopRated from "./components/TopRated";
import HomePage from "./components/HomePage";
import CoffeeDetail from "./components/CoffeeDetail";
import { useDispatch } from "react-redux";
import ShopDetails from "./components/Shop";
import { render } from "react-dom";

function App() {
  const dispatch = useDispatch()
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const render = async () => {
      const user = await dispatch(authenticate());
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    };
    render();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar
        authenticated={authenticated}
        setAuthenticated={setAuthenticated}
      />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/signup" exact={true}>
          <SignUpForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/" exact={true} authenticated={authenticated}>
          <Landing authenticated={authenticated} />
        </Route>
        <ProtectedRoute path="/coffeehouse" authenticated={authenticated}>
          <CoffeeHouse authenticated={authenticated}/>
        </ProtectedRoute>
        <ProtectedRoute path="/toprated">
          <TopRated />
        </ProtectedRoute>
        <ProtectedRoute path="/home" exact={true} authenticated={authenticated}>
          <HomePage authenticated={authenticated}/>
        </ProtectedRoute>
        <ProtectedRoute path="/coffees/:id" exact={true} authenticated={authenticated}>
          <CoffeeDetail />
        </ProtectedRoute>
        <ProtectedRoute path="/shop/:id" exact={true} authenticated={authenticated}>
          <ShopDetails />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
