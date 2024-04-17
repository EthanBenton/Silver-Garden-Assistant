import React from 'react';
import { Link } from 'react-router-dom';
import './GraphsPage0.css';

/**
 *  Used to display a static .html file name on the website
 */
const GraphsPage0 = () => {
  return (
    <div>
      <Link to="/">
        <button>Back</button>
      </Link>
      <h1>Simulated Data Visualization</h1>
      <p>Here is an interesting graph...</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/simulated_data.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage0;