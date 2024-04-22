import React from 'react';
import { Link } from 'react-router-dom';
import './GraphsPage7.css';

/**
 *  Used to display a static .html file name on the website
 */
const GraphsPage7 = () => {
  return (
    <div>
      <Link to="/">
        <button>Back</button>
      </Link>
      <h1>Graphs</h1>
      <p>Here are some interesting graphs...GraphsPage7</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/sensor_data.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage7;
