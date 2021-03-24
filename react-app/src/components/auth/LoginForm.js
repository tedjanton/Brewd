import React, { useState } from "react";
import { useDispatch } from 'react-redux';
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import "./LoginForm.css";


const LoginForm = ({ authenticated, setAuthenticated }) => {
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const user = await login(email, password);
    if (!user.errors) {
      setAuthenticated(true);
      dispatch(login(email, password))
    } else {
      setErrors(user.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login_form_container">
      <div className="login_form_white_background">
        <form  className="login_form"onSubmit={onLogin}>
          <div>
            {errors.map((error) => (
              <div>{error}</div>
            ))}
          </div>

          <div className="site_title">BREWD</div>
          <div className="saying_container">
            <p className="site_saying">S I P</p><p className="site_saying">S O C I A L L Y</p>
          </div>

          <button className="demo_user_login">
            <div className="demo_text_container">
              <p className="demo_text_small">Sign in as</p>
              <p className="demo_text_large">demo</p>
            </div>
          </button>

          <div className="circle_OR">OR</div>

          <div className="email_container">
            <i className="fas fa-user user_icon"></i>
            <input
              name="email"
              type="text"
              placeholder="Email"
              value={email}
              onChange={updateEmail}
              className="email_input"
            />
          </div>
          <div className="password_container">
            <i class="fas fa-lock password_icon"></i>
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={password}
              onChange={updatePassword}
              className="password_input"
            />
          </div>
          <div className="recaptcha_container">
            <div className="recaptcha_img" />
            <div>Privacy</div>
            <div>Terms</div>
          </div>
          <button type="submit" className="sign_in_button">Sign In</button>
        </form>
      </div>
    </div>
      
  );
};

export default LoginForm;
