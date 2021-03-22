import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getUserSips } from "../../store/coffeehouse.js";


const HomePage = ({ authenticated }) => {
    const dispatch = useDispatch();
    const userSips = useSelector(state => state.coffeehouse);
    const user = useSelector(state => state.user);

    useEffect(() => {
        if(user) {
            dispatch(getUserSips(user.id))
        }
    }, [user, dispatch])
   
    if(!authenticated) {
        return null;
    }
    console.log(userSips)

    return (
        <>
            <h1>Hello From HomePage</h1>
        </>
    )
}

export default HomePage;