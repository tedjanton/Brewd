// import React from "react";
// import { useDispatch, useSelector } from "react-redux";
// import { Redirect } from "react-router-dom";
// import { getSips } from "../../store/coffeehouse";
// import "./Dashboard.css";

// const coffeeHouse = ({ authenticated }) => {
//     if (!authenticated) {
//         return <Redirect to="/" />
//     }
//     const dispatch = useDispatch();
//     const sips = useSelector((state) => {
//         console.log("STATE", state);
//         return state.coffeeHouse
//     });
//     const handleSips = async () => {
//         const retrievePosts = await dispatch(getPosts())
//     }

//     return (
//         <>
//         <h2>Hello From Coffee House</h2>
//         </>
//     )
// }

// export default coffeeHouse;