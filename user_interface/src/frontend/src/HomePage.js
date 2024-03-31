import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

const HomePage = () => {
  const boxes = [
    { id: 1, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png` },
    { id: 2, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png` },
    { id: 3, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png` },
    { id: 4, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png` },
  ];

  return (
    <div className="containerStyle">
      {boxes.map((box) => (
        <Link to="/graphs" key={box.id} className="boxLink">
          <div className="boxStyle">
            <img src={box.imagePath} alt={`Graphs ${box.id}`} className="imageStyle" />
            <div className="boxFooter">
              Your Graphs
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
};

export default HomePage;

