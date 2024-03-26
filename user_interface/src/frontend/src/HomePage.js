import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  const boxes = [
    { id: 1, imagePath: `${process.env.PUBLIC_URL}/GraphPicForGraphsBox.png` },
    { id: 2, imagePath: `${process.env.PUBLIC_URL}/GraphPicForGraphsBox.png` },
    { id: 3, imagePath: `${process.env.PUBLIC_URL}/GraphPicForGraphsBox.png` },
    { id: 4, imagePath: `${process.env.PUBLIC_URL}/GraphPicForGraphsBox.png` },
  ];

  const boxStyle = {
    width: '400px',
    height: '440px',
    margin: '20px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#4CAF50',
    color: 'white',
    borderRadius: '10px',
    cursor: 'pointer',
    textDecoration: 'none',
  };

  const containerStyle = {
    display: 'grid',
    gridTemplateColumns: 'repeat(2, 1fr)', // Creates two columns, distributing space equally
    gap: '20px', // Adjusts the gap between grid items
    justifyContent: 'center',
    maxWidth: '860px', // Adjust as needed based on the box size and desired margins
    margin: 'auto',
  };

  const imageStyle = {
    width: '100%',
    height: '80%',
    objectFit: 'cover',
    borderRadius: '10px 10px 0 0',
  };

  return (
    <div style={containerStyle}>
      {boxes.map((box) => (
        <Link to="/graphs" key={box.id} style={{ textDecoration: 'none' }}>
          <div style={boxStyle}>
            <img src={box.imagePath} alt={`Graphs ${box.id}`} style={imageStyle} />
            <div style={{ width: '100%', height: '20%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              Your Graphs
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default HomePage;




