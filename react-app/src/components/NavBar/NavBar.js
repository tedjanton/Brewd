import React from "react";
import { NavLink } from "react-router-dom";
import LogoutButton from "../auth/LogoutButton";
import "./NavBar.css"
import ProfileButton from "./ProfileButton"

const NavBar = ({ authenticated, setAuthenticated }) => {
  let sessionLinks;
  if (authenticated) {
    sessionLinks = (
      <div className="navContainer ">
        <div className="yellowBar"></div>
      <nav className="flex-container-navbar">
        <ul className="flex-container-ul">
          <li>
            <NavLink className="brewd-letters" to="/" exact={true} activeClassName="active">
              BREWD
            </NavLink>
          </li>
          {/* <li>
            <NavLink to="/login" exact={true} activeClassName="active">
              Login
            </NavLink>
          </li>
          <li>
            <NavLink to="/signup" exact={true} activeClassName="active">
              Sign Up
            </NavLink>
          </li>
          <li>
            <NavLink to="/users" exact={true} activeClassName="active">
              Users
            </NavLink>
          </li> */}
          <li>
            <NavLink className="link-other-page" to="/coffeehouse" exact={true} activeClassName="active">
              Coffee House
            </NavLink>
          </li>
          <li>
            <NavLink className="link-other-page" to="/top_rated" exact={true} activeClassName="active">
              Top Rated
            </NavLink>
          </li>
          {/* <li className="rightAlign">

          </li> */}
          {/* <li>
            <LogoutButton setAuthenticated={setAuthenticated} />
          </li> */}
        </ul>
        <ProfileButton className="profile-button-nav" setAuthenticated={setAuthenticated}/>
      </nav>

      </div>
    );
  } else {
    sessionLinks = <></>;
  }

  return <>{sessionLinks}</>;
};

export default NavBar;
