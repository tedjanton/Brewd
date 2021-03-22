import React from "react";
import { NavLink, Redirect } from "react-router-dom";
import "./Landing.css";

const Landing = ({ authenticated }) => {

    if (authenticated) {
        return <Redirect to="/home" />
    }

    return (
        <>
            <div className="landing-background-container">
                <div className="landing-button-container">
                    <div className="landing-button-div login-button">
                        <NavLink to="/login">SIGN IN</NavLink>
                    </div>
                    <div className="landing-button-div login-button">
                        <NavLink to="/signup">CREATE AN ACCOUNT</NavLink>
                    </div>
                </div>
                <div className="landing-container">
                    <div className="landing-container-left">
                        <div className="landing-logo">
                            <i class="fas fa-coffee"></i>
                        </div>
                        <div className="landing-site-title">
                            <h1>BREWD</h1>
                        </div>
                        <div className="landing-subtitle">
                            <p>DRINK SOCIALLY</p>
                        </div>
                        <div className="landing-color-divider"></div>
                        <div className="landing-message">
                            <h1>Discover and share your favorite coffee.</h1>
                        </div>
                    </div>
                    <div className="landing-container-right">
                        <div className="landing-mobile-img">
                            <img src="https://untappd.akamaized.net/assets/custom/homepage/images/masthead-img-main.png" />
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
};

export default Landing;
