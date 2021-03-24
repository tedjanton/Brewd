import React, { useState } from "react";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import { useDispatch } from "react-redux";
import Recaptcha from "./Recaptcha"
import "./SignUpForm.css"
const SignUpForm = ({ authenticated, setAuthenticated }) => {
  const dispatch = useDispatch();
  const [username, setUsername] = useState("");
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const user = await dispatch(
        signUp(username, first_name, last_name, email, password)
      );
      if (!user.errors) {
        setAuthenticated(true);
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const updateLastName = (e) => {
    setLastName(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="form_container">
      <form onSubmit={onSignUp}>
        <div className="inputs_container">
          <div className="username_container">
            <label>User Name</label>
            <input
              type="text"
              name="username"
              onChange={updateUsername}
              value={username}
              placeholder="Username"
              ></input>
          </div>
          <div className="firstname_container">
            <input
              type="text"
              name="firstName"
              onChange={updateFirstName}
              value={first_name}
              placeholder="First Name"
              ></input>
          </div>
          <div className="lastname_container">
            <input
              type="text"
              name="lastName"
              onChange={updateLastName}
              value={last_name}
              placeholder="Last Name"
              ></input>
          </div>
          <div className="email_container">
            <i className="fas fa-user user_icon"></i>
            <input
              type="text"
              name="email"
              onChange={updateEmail}
              value={email}
              placeholder="Email Address"
              ></input>
          </div>
          <div className="password_container">
            <i class="fas fa-lock password_icon"></i>
            <input
              type="password"
              name="password"
              onChange={updatePassword}
              value={password}
              placeholder="Password"
              ></input>
          </div>
          <div className="repeatpassword_container">
            <i class="fas fa-lock password_icon"></i>
            <input
              type="password"
              name="repeat_password"
              onChange={updateRepeatPassword}
              value={repeatPassword}
              required={true}
              placeholder="Repeat Password"
              ></input>
          </div>
        </div>
        <Recaptcha />
        <p className="above_button_phrase"></p>
        <button type="submit" className="sign_up_button">Sign Up</button>
      </form>
    </div>
  );
};

export default SignUpForm;
