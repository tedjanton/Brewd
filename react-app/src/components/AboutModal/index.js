import React from 'react';
import tedanton from '../../site-images/tedanton.jpeg';
import oliviayoung from '../../site-images/oliviayoung.jpeg';
import laurenchambers from '../../site-images/laurenchambers.jpeg';
import rajhudek from '../../site-images/rajhudek.jpeg';
import './AboutModal.css';

const AboutModal = () => {

  return (
    <div className="about-modal">
      <h1>About the Developers</h1>
      <div className="all-devs-container">
        <div className="dev-container" id="dev-1">
          <img src={tedanton} alt="Ted Anton" />
          <p>Ted Anton</p>
            <a href='https://github.com/tedjanton' target="_blank" rel="noopener noreferrer">
              <i className="fab fa-github" />
            </a>
            <a href="https://www.linkedin.com/in/ted-anton/" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-linkedin" />
            </a>
        </div>
        <div className="dev-container" id="dev-2">
          <img src={oliviayoung} alt="Olivia Young" />
          <p>Olivia Young</p>
            <a href='https://github.com/olivianicole' target="_blank" rel="noopener noreferrer">
              <i className="fab fa-github" />
            </a>
            <a href="https://www.linkedin.com/in/olivia-young-2437ba1b9/" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-linkedin" />
            </a>
        </div>
        <div className="dev-container" id="dev-3">
          <img src={laurenchambers} alt="Lauren Chambers" />
          <p>Lauren Chambers</p>
            <a href='https://github.com/laurenchambers' target="_blank" rel="noopener noreferrer">
              <i className="fab fa-github" />
            </a>
            <a href="https://www.linkedin.com/in/lauren-chambers94/" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-linkedin" />
            </a>
        </div>
        <div className="dev-container" id="dev-4">
          <img src={rajhudek} alt="Raj Hudek" />
          <p>Raj Hudek</p>
            <a href='https://github.com/LifeJunkieRaj' target="_blank" rel="noopener noreferrer">
              <i className="fab fa-github" />
            </a>
            <a href="https://www.linkedin.com/in/raj-hudek-026b051b1/" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-linkedin" />
            </a>
        </div>
      </div>
    </div>
  )
};

export default AboutModal;
