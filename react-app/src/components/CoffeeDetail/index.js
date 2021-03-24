import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { Modal } from "../../context/Modal";
import { getCoffee } from "../../store/coffee-detail";
import SipForm from "../SipModal/SipForm";
import Coffee from "../Coffee";
import Sip from "../Sip";
import { getSips } from "../../store/coffeehouse";


const CoffeeDetail = () => {
    const params = useParams();
    const dispatch = useDispatch();
    const [showModal, setShowModal] = useState();

    const coffee = useSelector((state) => {
       return state.selected?.coffee?.currentCoffee;
    })
    console.log("COFFEEFFFFFE", coffee)
    const sips = useSelector((state) => {
        return state.coffeehouse?.sips?.all_sips;
    })

    useEffect(() => {
        if (!coffee) {
            dispatch(getCoffee(params.id))
        }
        if (!sips) {
            dispatch(getSips())
        }
    }, [coffee, sips, dispatch])
    return (
        <>
            <Coffee coffee={coffee} />
            <button onClick={() => setShowModal(true)}>Sip Coffee</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <SipForm />
                </Modal>
            )}
            <div className="coffee_sips_container">
                {sips?.map((sip) => (
                            <Sip sip={sip} />
                        ))}
            </div>
            
        </>
    )
}

export default CoffeeDetail;
