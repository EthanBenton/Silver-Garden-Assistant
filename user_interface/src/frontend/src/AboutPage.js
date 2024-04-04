import React from 'react';
import './AboutPage.css';

const AboutPage = () => {
  return (
    <div className="containerStyle">
      <p className="leadTextStyle lead">
      <h2>What is PRIA</h2>
        PRIA is a self-hosted web application garden management system to aid gardeners, either new or experienced. 
        It aims to provide gardeners with the necessary tools to know when to plant, manage nutrients and water content in the soil,
        and better improve their gardening capabilities while improving their plant’s health and growth.
      </p>
      <div className="marginTop40">
        <h2>How it works</h2>
      </div>
      <div className="row justify-content-center marginTop20">
        <div className="col-lg-6">
          <p className="leadTextStyle lead">
            First, data is collected on the weather and the plants then passed to the IOT sensors.
            Next, it is ran into a MCU and then stored into SQLite, a database. 
            Following the storing of the data Pandas and NumPy is to format the data.
            Once the data is uniformly sorted, PyTorch and Scikit start the machine learning process.
            After feeding the data into machine learning it is simultaneously being visualized with Matplotlib, Seaborn and Plotly
            while using regression models and reinforcement learning to help predict future trends and adjust for the best results.
            Finally, the data has been collected, processed and visualized. 
            Feedback is provided on the user interface using flask and react.
          </p>
          <img 
            src={`${process.env.PUBLIC_URL}/images/MFCD.png`} 
            alt="How it works" 
            className="imageStyle img-fluid"
          />
        </div>
      </div>
    </div>
  );
};

export default AboutPage;




