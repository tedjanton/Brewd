import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { Modal } from "../../context/Modal";
import SipForm from "../SipModal/SipForm";
import { getCoffee } from "../../store/coffee-detail";
import IndividualCoffee from "../IndividualCoffee";
import Sip from "../Sip";
import { getCoffeeSips } from "../../store/coffeehouse";
import { getUserLikes } from "../../store/like";
import "./CoffeeDetail.css";

const CoffeeDetail = () => {
    const params = useParams();
    const dispatch = useDispatch();
    const [showModal, setShowModal] = useState();
    const user = useSelector(state => state.session.user)
    const coffeeSips = useSelector(state => state.coffeehouse?.sips?.coffeeSips);
    const coffee = useSelector((state) => state.selected?.coffee?.currentCoffee);

    useEffect(() => {
        dispatch(getCoffee(params.id))
        dispatch(getCoffeeSips(params.id));
        dispatch(getUserLikes(user.id))
    }, [dispatch, params, user])

    return (
        <div className="coffee_details_page_container">
            <div className="coffee_details_page_container_top">
                <div className="individual_coffee_container">
                    <IndividualCoffee coffee={coffee} />
                </div>
                <div className="cd_middle_container">
                    <p className="coffee_description_i">{coffee?.description}</p>
                    <button
                        onClick={() => setShowModal(true)}
                        className="make_new_post">
                        <i className="fas fa-coffee mug_icon" />
                    </button>
                    {showModal && (
                        <Modal onClose={() => setShowModal(false)}>
                            <SipForm coffee={coffee} setShowModal={setShowModal} />
                        </Modal>
                    )}
                </div>
            </div>
            <div className="coffee_details_page_bottom">
            {coffeeSips?.map((sip) => (
                <div key={sip.id} className="coffee_details_page_container_bottom">
                    <Sip key={sip.id} sip={sip} coffee={coffee} />
                </div>
            ))}
            </div>
        </div>
    )
}


export default CoffeeDetail;
