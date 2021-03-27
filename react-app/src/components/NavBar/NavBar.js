import React from "react";
import { NavLink } from "react-router-dom";
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
          <li>
            <NavLink className="link-other-page" to="/coffeehouse" exact={true} activeClassName="active">
              Coffee House
            </NavLink>
          </li>
          <li>
            <NavLink className="link-other-page" to="/toprated" exact={true} activeClassName="active">
              Top Rated
            </NavLink>
          </li>
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
