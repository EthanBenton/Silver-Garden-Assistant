import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';


/**
 * HomePage display the home page content
 */
const HomePage = () => {

  // Data for boxes with images and links with text ontop
  const boxes = [
    { id: 1, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png`, path: "/graphs0", footerName: "Interactive Graphs" },
    { id: 2, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png`, path: "/graphs1", footerName: "Data in Tables" },
    { id: 3, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png`, path: "/graphs2", footerName: "graphs2" },
    { id: 4, imagePath: `${process.env.PUBLIC_URL}/images/GraphPicForGraphsBox.png`, path: "/graphs3", footerName: "Regression Model" },
  ];

  return (
    <div className="containerStyle">
      <div className="welcomeText">Welcome Back, Thomas</div> 
      <div className="boxesContainer">
        {boxes.map((box) => (
          <Link to={box.path} key={box.id} className="boxLink">
            <div className="boxStyle">
              <img src={box.imagePath} alt={`Graphs ${box.id}`} className="imageStyle" />
              <div className="boxFooter">{box.footerName}</div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default HomePage;



