import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { Modal } from "../../context/Modal";
import { getCoffee } from "../../store/coffee-detail";
import SipForm from "../SipModal/SipForm";


const CoffeeDetail = () => {
    const params = useParams();
    const dispatch = useDispatch();
    const [showModal, setShowModal] = useState();

    let coffee;
    useEffect(() => {
        if (!coffee) {
            coffee = dispatch(getCoffee(params.id))
        }
    })

    return (
        <>
            <h1>Coffee Detail</h1>
            <button onClick={() => setShowModal(true)}>Sip Coffee</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <SipForm />
                </Modal>
            )}
        </>
    )
}

export default CoffeeDetail;
