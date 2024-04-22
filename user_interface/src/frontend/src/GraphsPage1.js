import React from 'react';
import { Link } from 'react-router-dom';
import './GraphsPage1.css';

/**
 *  Used to display a static .html file name on the website
 */
const GraphsPage1 = () => {
  return (
    <div>
      <Link to="/">
        <button>Back</button>
      </Link>
      <h1>Data in Tables</h1>
      <p>Here are some interesting tables...GraphsPage1</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/DataTables.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage1;
