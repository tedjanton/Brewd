import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect } from "react-router";
import { getUserSips } from "../../store/coffeehouse";
import { authenticate } from "../../store/session"


const HomePage = ({ authenticated }) => {
    const dispatch = useDispatch();
    const sips = useSelector(state => state.coffeehouse);
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        if (!user) dispatch(authenticate())
        if (user && !sips[0]?.user_sip) {
            dispatch(getUserSips(user.id))
        }
    }, [user, dispatch])

    return (
        <>
            <h1>Hello From HomePage</h1>
        </>
    )
}

export default HomePage;
