import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getUserSips } from "../../store/coffeehouse";
import { authenticate } from "../../store/session";
import Sip from "../../components/Sip";
import user_icon from "../../site-images/user_icon.jpeg";
import "./HomePage.css";


const HomePage = ({ authenticated }) => {
    const dispatch = useDispatch();
    const sips = useSelector(state => state.coffeehouse?.sips?.user_sips);
    const user = useSelector(state => state.session.user);

    const unique = new Set(sips?.map(sip => sip.coffee_id));

    useEffect(() => {
        if (!user) dispatch(authenticate())
        if (user && !sips?.user_sip) {
            dispatch(getUserSips(user.id))
        }
    }, [user, dispatch])

    return (
        <div className="home-container">
            <div className="home-feed-container">
                <div className="home-feed-title">My Recent Activity
                </div>
                <div className="home-sips-container">
                    {sips?.map(sip => (
                        <Sip key={sip.id} sip={sip} />
                    ))}
                </div>
            </div>
            <div className="home-user-container">
                <div className="home-user-icon">
                    <img src={user_icon} />
                </div>
                <div className="home-user-name">
                    <p>{`${user.first_name} ${user.last_name}`}</p>
                </div>
                <div className="home-user-username">
                    <i class="fas fa-user" />
                    <p>{user.username}</p>
                </div>
                <div className="home-user-sip-container">
                    <div className="home-user-sip-count">
                        <p>{sips?.length}</p>
                        <div className="home-user-sip-count-subtitle">
                            <p>TOTAL SIPS</p>
                        </div>
                    </div>
                    <div className="home-user-sip-unique-count">
                        <p>{unique.size}</p>
                        <div className="home-user-sip-unique-count-subtitle">
                            <p>TOTAL UNIQUE SIPS</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HomePage;