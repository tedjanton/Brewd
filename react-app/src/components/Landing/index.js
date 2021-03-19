import React from "react"
import { NavLink } from "react-router-dom"
import "./Landing.css"


const Landing = () => {

    return (
        <>
            <h1>Hello from Landing Page</h1>
            <div className="sign-in-button">
                <NavLink to="/login">Sign In</NavLink>
            </div>
            <div className="create-account-button">
                <NavLink to="/signup">Create Account</NavLink>
            </div>
        </>
    )
}


export default Landing;
