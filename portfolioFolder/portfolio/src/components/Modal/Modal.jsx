import React from 'react'
import Modal from 'react-modal'
import './Modal.css'
import '../Hero/Intro.css'

Modal.setAppElement('#root');

function Modals({ detail }) {
    const [modalIsOpen, setIsOpen] = React.useState(false);



    function openModal() {
        setIsOpen(true);
    }

    function afterOpenModal() {
        // references are now sync'd and can be accessed.
        //   subtitle.style.color = '#f00';
    }

    function closeModal() {
        setIsOpen(false);
    }
    return (
        <div >
            <button onClick={openModal} className="contact-me">
                Hire me! <i class="bx bx-send "></i>
            </button>
            {/* <button onClick={openModal}>Open Modal</button> */}
            <Modal
                isOpen={modalIsOpen}
                onAfterOpen={afterOpenModal}
                onRequestClose={closeModal}
                style={{
                    overlay: {
                        position: 'fixed',
                        top: 0,
                        left: 0,
                        right: 0,
                        bottom: 0,
                        backgroundColor: 'rgba(255, 255, 255, 0.75)',
                        zIndex:999,
                    },
                    content: {
                        position: 'absolute',
                        top: '100px',
                        left: '40px',
                        right: '40px',
                        bottom: '40px',
                        border: '1px solid #ccc',
                        backgroundColor: 'rgb(245,245,242)',
                        overflow: 'auto',
                        WebkitOverflowScrolling: 'touch',
                        borderRadius: '4px',
                        outline: 'none',
                        padding: '20px'
                    }
                }}
                contentLabel="Hire me Modal"
            >
                <div>
                    <div className='flex'>
                        <h2 className='display-2'>Hello</h2>
                        <button onClick={closeModal}>x</button>
                    </div>
                    <p className='h2'>I am a modal</p>
                    <form className='.container-xl'>
                        <div className='form-group'>
                            <input class="form-control form-control-lg" type="text" placeholder="Enter Your Email!"></input>
                        </div>
                        {/* <button>tab navigation</button> */}
                        {/* <button>stays</button> */}
                        {/* <button>inside</button> */}
                        {/* <button>the modal</button> */}
                    </form>
                        <a href={`mailto:${detail.emailAddress}`} className="contactMe">
                            <button className="contact-me btn-custom">
                                Hire me! <i class="bx bx-send "></i>
                            </button>
                        </a>
                </div>
            </Modal>
        </div>
    )
}

export default Modals

