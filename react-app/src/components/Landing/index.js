import React from "react";
import { NavLink, Redirect } from "react-router-dom";

const Landing = ({ authenticated }) => {

    if (authenticated) {
        return <Redirect to="/home" />
    }

    return (
        <>
            <h1>Hello from Landing</h1>
            <div>
                <NavLink to="/login">SIGN IN</NavLink>
            </div>
            <div>
                <NavLink to="/signup">CREATE AN ACCOUNT</NavLink>
            </div>
        </>
    )
};

export default Landing;
