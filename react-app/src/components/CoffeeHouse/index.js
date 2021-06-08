import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getSips } from "../../store/coffeehouse";
import { getUserLikes } from "../../store/like";
import "./CoffeeHouse.css";
import Sip from "../Sip";
import Featured from "../Featured";

const CoffeeHouse = () => {
  const dispatch = useDispatch();
  const sips = useSelector((state) => state.coffeehouse?.sips?.all_sips);
  const user = useSelector(state => state.session.user);
  const [loading, setIsLoading] = useState(true);

  const getAllSips = async () => {
    await dispatch(getSips());
    setIsLoading(false);
  }

  useEffect(() => {
    getAllSips();
    dispatch(getUserLikes(user.id))
  // eslint-disable-next-line
  }, [dispatch, user]);


  return (
    <div className="coffeehouse_container">
      <div className="sip_container">
        <div className="page_title">Recent Global Activity</div>
        {loading ? (
          <div className="loader">
            <div className="loader-spinner"></div>
          </div>
        ) : (
          <>
          {sips?.map((sip) => (
            <Sip key={sip.id} sip={sip} />
          ))}
          </>
        )}
      </div>
        <Featured />
      </div>
    )
}

export default CoffeeHouse;
