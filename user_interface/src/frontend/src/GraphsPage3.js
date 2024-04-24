/* eslint-disable jsx-a11y/img-redundant-alt */
import React from 'react';
import { Link } from 'react-router-dom';
import './GraphsPage3.css';

/**
 *  Used to display a static .html file name on the website
 */
const GraphsPage3 = () => {
  return (
    <div>
      <Link to="/">
        <button>Back</button>
      </Link>
      <h1>Regression model Graphs</h1>
      <p>Here are some interesting Regression model graphs...GraphsPage3</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/regression_model.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>      
      

    </div>
  );
};

export default GraphsPage3;
