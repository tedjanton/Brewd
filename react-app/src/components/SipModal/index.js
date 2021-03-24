import React, { useState } from "react";
import { Modal } from "../../context/Modal";
import SipForm from "./SipForm";


const SipFormModal = ({ }) => {
    const [showModal, setShowModal] = useState(false);


    return (
        <>
            <button onClick={() => setShowModal(true)}></button>
        </>
    )
}
