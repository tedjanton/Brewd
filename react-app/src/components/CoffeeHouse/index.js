import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeHouse.css";
import Sip from "../Sip";
import Featured from "../Featured";
import CommentForm from "../Comment/index";

const CoffeeHouse = ({ authenticated }) => {
  const dispatch = useDispatch();
  const sips = useSelector((state) => {
    return state.coffeehouse?.sips?.all_sips;
  });

  useEffect(() => {
    if (!sips) {
      dispatch(getSips());
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
