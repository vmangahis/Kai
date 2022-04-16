import {useState} from 'react';
import Backdrop from './Backdrop';
import Modal from './Modal';

function Card(props){

const [modalOpen, setModalOpen] = useState(false);

function addToCollection(){
    setModalOpen(true);
}

function closeModal(){
    setModalOpen(false);
}

    return (<>
    <div className="card">
        <button className="image-clickable" onClick={addToCollection}/>
        <h2>{props.title}</h2>
        <p>Description</p>
       
    </div>
    {modalOpen &&  <Modal />}
    {modalOpen &&  <Backdrop onClose={closeModal}/>}
    
    </>
    
    );
    
}

export default Card;