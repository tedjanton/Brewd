import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { Modal } from "../../context/Modal";
import SipForm from "../SipModal/SipForm";
import { getCoffee } from "../../store/coffee-detail";
import IndividualCoffee from "../IndividualCoffee";
import IndividualSip from "../IndividualSip";
import { getSips } from "../../store/coffeehouse";
import "./CoffeeDetail.css";

const CoffeeDetail = () => {
  const params = useParams();
  const dispatch = useDispatch();
  const [showModal, setShowModal] = useState();

  const coffee = useSelector((state) => {
    return state.selected?.coffee?.currentCoffee;
  });

  const sips = coffee?.sips;

    useEffect(() => {
        if (!coffee) {
            dispatch(getCoffee(params.id))
        }
        if (!sips) {
            dispatch(getSips())
        }
    }, [coffee, sips, dispatch, params])

    return (
        <div className="coffee_details_page_container">
            <div className="coffee_details_page_container_top">
                <div className="individual_coffee_container">
                    <IndividualCoffee coffee={coffee} />
                </div>
                <div className="cd_middle_container">
                    <p className="coffee_description_i">{coffee?.description}</p>
                    <button onClick={() => setShowModal(true)} className="make_new_post"><i className="fas fa-coffee mug_icon"></i></button>
                    {showModal && (
                        <Modal onClose={() => setShowModal(false)}>
                            <SipForm coffee={coffee} setShowModal={setShowModal} />
                        </Modal>
                    )}
                </div>
            </div>
            <div className="coffee_details_page_container_bottom">
                <div>
                    {sips?.map((sip) => (
                        <IndividualSip key={sip.id} sip={sip} coffee={coffee} />
                    ))}
                </div>
            </div>

        </div>
    )
}


export default CoffeeDetail;
