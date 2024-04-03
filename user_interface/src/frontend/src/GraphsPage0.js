import React from 'react';
import './GraphsPage.css';
const GraphsPage0 = () => {
  return (
    <div>
      <h1>Graphs</h1>
      <p>Here are some interesting graphs...</p>
      <iframe src={`${process.env.PUBLIC_URL}/graphs/sensor_data.html`} title="Graphs" style={{width: '100%', height: '600px', border: 'none'}}></iframe>
    </div>
  );
};

export default GraphsPage0;
