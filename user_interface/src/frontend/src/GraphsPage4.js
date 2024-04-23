import React from 'react';
import { Link } from 'react-router-dom';
import './GraphsPage4.css';

/**
 *  Used to display a static .html file name on the website
 */
const GraphsPage4 = () => {
  return (
    <div>
      <Link to="/">
        <button>Back</button>
      </Link>
      <h1>Graphs</h1>
      <p>Here are some interesting graphs...GraphsPage4</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/regression_model(1).html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage4;
