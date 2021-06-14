import { NavLink } from "react-router-dom";
import React, {useState, useEffect} from 'react';
import LogoutButton from "../../components/auth/LogoutButton"
import user_icon from "../../site-images/user_icon.png";
import "./ProfileButton.css"


function ProfileButton({ setAuthenticated }) {
    const [showMenu, setShowMenu]= useState(false);

    const closeMenu = () => {
        setShowMenu(false);
    };

    const openMenu = () => {
        if (showMenu) {
            setShowMenu(false);
        } else {
            setShowMenu(true);
        }
    };

    useEffect(() => {
        if (!showMenu) return;

        document.addEventListener("mouseEnter", closeMenu);

        return () => document.removeEventListener("mouseEnter", closeMenu);
    }, [showMenu]);


    return (
        <div className="menuContainer">
            <img className="profileImg" src={user_icon} alt="" onClick={openMenu} />
            {showMenu && (
            <div onClick={closeMenu} className="menu">
                <NavLink  to="/"exact={true} className="dropdown-item">Profile</NavLink>
                <NavLink to="/coffeehouse" exact={true} className="dropdown-item">Coffee Shop</NavLink>
                <NavLink to="/toprated" exact={true} className="dropdown-item">Top Rated</NavLink>
                <LogoutButton setAuthenticated={setAuthenticated} />
            </div> ) }
        </div>

    )
}

export default ProfileButton
