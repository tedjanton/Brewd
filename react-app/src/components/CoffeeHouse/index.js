import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getSips } from "../../store/coffeehouse";
import { getUserLikes } from "../../store/like";
import "./CoffeeHouse.css";
import Sip from "../Sip";
import Featured from "../Featured";

const CoffeeHouse = ({ authenticated }) => {
  const dispatch = useDispatch();
  const sips = useSelector((state) => {
    return state.coffeehouse?.sips?.all_sips;
  });
  const user = useSelector(state => state.session.user)

  useEffect(() => {
    if (!sips) {
      dispatch(getSips());
      dispatch(getUserLikes(user.id))
    }
  }, [sips, dispatch]);

     return (
        <div className="coffeehouse_container">
            <div className="sip_container">
                <div className="page_title">Recent Global Activity</div>
                    {sips?.map((sip) => (
                        <Sip key={sip.id} sip={sip} />
                    ))}
            </div>
            <Featured />
        </div>
    )
}


export default CoffeeHouse;
