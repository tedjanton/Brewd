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
      <div className="form_white_background">
        <form className="form" onSubmit={onSignUp}>
          <div className="site_title">BREWD</div>
          <div className="saying_container">
            <p className="site_saying">S I P</p><p className="site_saying">S O C I A L L Y</p>
          </div>
          <div className="inputs_container">
            <div className="coffeeshop_message">
              <p className="coffeeshop_message_text_1">Are you a coffee shop that would like to get added to Brewd and be able to claim and manage your shop's page? Coming soon: </p>
              <p className="coffeeshop_message_text_2">Getting on Brewd: Shop Guide</p>
            </div>
            <div className="message1">All fields below are required.</div>
            <div className="message2">Avoid using common words and include a mix of letters and numbers.</div>
            <div className="username_container">
              <i className="fas fa-user user_icon"></i>
              <input
                type="text"
                name="username"
                onChange={updateUsername}
                value={username}
                placeholder="Username"
                className="username_input"
                ></input>
            </div>
            <div className="firstname_container">
              <input
                type="text"
                name="firstName"
                onChange={updateFirstName}
                value={first_name}
                placeholder="First Name"
                className="firstname_input"
                ></input>
            </div>
            <div className="lastname_container">
              <input
                type="text"
                name="lastName"
                onChange={updateLastName}
                value={last_name}
                placeholder="Last Name"
                className="lastname_input"
                ></input>
            </div>
            <div className="email_container">
              <i className="fas fa-envelope email_icon"></i>
              <input
                type="text"
                name="email"
                onChange={updateEmail}
                value={email}
                placeholder="Email Address"
                className="email_input"
                ></input>
            </div>
            <div className="password_container">
              <i className="fas fa-lock password_icon"></i>
              <input
                type="password"
                name="password"
                onChange={updatePassword}
                value={password}
                placeholder="Password"
                className="password_input"
                ></input>
            </div>
            <div className="repeatpassword_container">
              <i className="fas fa-lock password_icon"></i>
              <input
                type="password"
                name="repeat_password"
                onChange={updateRepeatPassword}
                value={repeatPassword}
                required={true}
                placeholder="Repeat Password"
                className="repeatedpassword_input"
                ></input>
            </div>
          </div>
          <Recaptcha />
          <p className="above_button_phrase">You must be a dedicated coffee drinker in your country to join Brewd. By Clicking Create Account, you agree to love coffee forever.</p>
          <button type="submit" className="form_button">Account</button>
        </form>
      </div>
    </div>
  );
};

export default SignUpForm;
