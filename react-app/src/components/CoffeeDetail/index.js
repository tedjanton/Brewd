import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { Modal } from "../../context/Modal";
import SipForm from "../SipModal/SipForm";


const CoffeeDetail = () => {
    const params = useParams();
    const [showModal, setShowModal] = useState();


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
