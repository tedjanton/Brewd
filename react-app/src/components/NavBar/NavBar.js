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
      <nav className="flex-container navBar">
        <ul className="flex-container navUl">
          <li>
            <NavLink className="brewd-letters" to="/" exact={true} activeClassName="active">
              Brewd
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
            <NavLink to="/coffeehouse" exact={true} activeClassName="active">
              Coffee House
            </NavLink>
          </li>
          <li>
            <NavLink to="/top_rated" exact={true} activeClassName="active">
              Top Rated
            </NavLink>
          </li>
          {/* <li className="rightAlign">
            
          </li> */}
          {/* <li>
            <LogoutButton setAuthenticated={setAuthenticated} />
          </li> */}
        </ul>
        <ProfileButton className="rightAlign"/>
      </nav>
      
      </div>
    );
  } else {
    sessionLinks = <></>;
  }

  return <>{sessionLinks}</>;
};

export default NavBar;
