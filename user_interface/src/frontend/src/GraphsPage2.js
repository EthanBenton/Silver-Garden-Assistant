import React from 'react';
import { Link } from 'react-router-dom';
import './GraphsPage2.css';

/**
 *  Used to display a static .html file name on the website
 */
const GraphsPage2 = () => {
  return (
    <div>
      <Link to="/">
        <button>Back</button>
      </Link>
      <h1>Watering Schedule</h1>
      <p>Here is an interesting table...GraphsPage2</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/watering_schedule.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage2;
