import React from 'react';
import styles from './AboutPage.css';

/**
 * AboutPage to display the product content
 */
const AboutPage = () => {
  
  return (
    <div className="aboutContainerStyle">
      <div className="row align-items-center">
        <div className="col-md-6">
          <div className="leftTextStyle lead">
            <h2>WHAT IS PRIA?</h2>
            PRIA, Personal Resource Irrigation Assistant, is a self-hosted web application garden management system to aid gardeners, either new or experienced. 
            It aims to provide gardeners with the necessary tools to know when to plant, manage nutrients and water content in the soil,
            and better improve their gardening capabilities while improving their plant’s health and growth.
          </div>
        </div>
        <div className="col-md-6">
          <img 
              src={`${process.env.PUBLIC_URL}/images/PRIA.png`} 
              alt="PRIA Logo" 
              className="aboutImageStyle img-fluid"
          />
        </div>
      </div>
      <div className="row justify-content-center marginTop40">
        <div className="col-lg-8 col-md-12 order-md-2">
          <div className="rightTextStyle lead">
            <h2>HOW IT WORKS</h2>
            First, data is collected on the weather and the plants then passed to the IOT sensors. Next, it is ran into a MCU and then stored into SQLite, a database. 
            Following the storing of the data Pandas and NumPy is to format the data.
            Once the data is uniformly sorted, PyTorch and Scikit start the machine learning process.
            After feeding the data into machine learning it is simultaneously being visualized with Matplotlib, Seaborn and Plotly
            while using regression models and reinforcement learning to help predict future trends and adjust for the best results.
            Finally, the data has been collected, processed and visualized. 
            Feedback is provided on the user interface using Flask and React.
          </div>
        </div>
        <div className="col-lg-4 col-md-12 order-md-1">
          <img 
            src={`${process.env.PUBLIC_URL}/images/MFCD.png`} 
            alt="How it works" 
            className="largeImageStyle img-fluid"
          />
        </div>
      </div>
      <div className="row justify-content-center marginTop40">
        <div className="col-12">
          <iframe 
            src="https://docs.google.com/presentation/d/e/2PACX-1vTFiBwp1e1skWucbLPoIp1q5X92NLZA35hxVR4pT87zAstJct-qOyhQNvZOln2KZ2g4kqwMVGQjUn00/embed?start=false&loop=false&delayms=3000" 
            frameborder="0" 
            width="960" 
            height="569" 
            allowfullscreen="true" 
            mozallowfullscreen="true" 
            webkitallowfullscreen="true">
          </iframe>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;