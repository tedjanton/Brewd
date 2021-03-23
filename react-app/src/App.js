import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import Landing from "./components/Landing";
import CoffeeHouse from "./components/CoffeeHouse"
import { authenticate } from "./store/session";
import TopRated from "./components/TopRated";
import HomePage from "./components/HomePage";
import { useDispatch } from "react-redux";

function App() {
  const dispatch = useDispatch()
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async () => {
      const user = await dispatch(authenticate());
      
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    })();
  }, []);

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
        <ProtectedRoute
          path="/users"
          exact={true}
          authenticated={authenticated}
        >
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute
          path="/users/:userId"
          exact={true}
          authenticated={authenticated}
        >
          <User />
        </ProtectedRoute>
        <Route path="/" exact={true} authenticated={authenticated}>
          <Landing authenticated={authenticated} />
        </Route>
        <Route path="/coffeehouse" authenticated={authenticated}>
          <CoffeeHouse authenticated={authenticated}/>
        </Route>
        <Route path="/top_rated">
          <TopRated />
        </Route>
        <ProtectedRoute path="/home" exact={true} authenticated={authenticated}>
          <HomePage authenticated={authenticated}/>
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
