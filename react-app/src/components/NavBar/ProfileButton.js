import user_icon from "../../site-images/user_icon.jpeg";

import React, {useState, useEffect} from 'react'
import "./ProfileButton.css"

import { NavLink } from "react-router-dom";





function ProfileButton() {

    const [showMenu,setShowMenu]= useState(false);
    const closeMenu = () => {
        setShowMenu(false);
      };
    
    const openMenu = () => {
       
        if(showMenu){
            setShowMenu(false);
        }else{
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
            {showMenu && (  <div className="menu" >
           
                
                <div onClick={closeMenu}><NavLink  to="/"exact={true} className="dropdown-item">Profile</NavLink></div>
                <div onClick={closeMenu}><NavLink to="/coffeehouse" exact={true} >Coffee Shop</NavLink></div>
                <div  onClick={closeMenu}><NavLink to="top_rated" exact={true} >Top Rated</NavLink></div>
                <div  onClick={closeMenu}><NavLink to="/logout" exact={true} >Logout</NavLink></div>
                
            </div> ) }
            
        </div>

    )
}

export default ProfileButton


