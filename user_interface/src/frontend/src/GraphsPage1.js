import React from 'react';
import './GraphsPage1.css';
const GraphsPage1 = () => {
  return (
    <div>
      <h1>Graphs</h1>
      <p>Here are some interesting graphs...</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/DataTables.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage1;
