import React from 'react';
import { Link } from 'react-router-dom';
import styles from './HomePage.css';


/**
 * HomePage display the home page content
 */
const HomePage = () => {

  // Data for boxes with images and links with text ontop
  const boxes = [
    { id: 1, imagePath: `${process.env.PUBLIC_URL}/images/dotgraph.png`, path: "/graphs0", footerName: "Simulated Data Visualization" },
    { id: 2, imagePath: `${process.env.PUBLIC_URL}/images/TableGraph.png`, path: "/graphs1", footerName: "Data in Tables" },
    { id: 3, imagePath: `${process.env.PUBLIC_URL}/images/watering.png`, path: "/graphs2", footerName: "Watering Schedule" },
    { id: 4, imagePath: `${process.env.PUBLIC_URL}/images/linear.png`, path: "/graphs3", footerName: "Regression Model" },
    { id: 5, imagePath: `${process.env.PUBLIC_URL}/images/poly.png`, path: "/graphs4", footerName: "Polynomial Regression" },
    { id: 6, imagePath: `${process.env.PUBLIC_URL}/images/RANSAC.png`, path: "/graphs5", footerName: "RANSAC Regression" },
    { id: 7, imagePath: `${process.env.PUBLIC_URL}/images/Clustering.png`, path: "/graphs6", footerName: "K-Means Clustering" },
    { id: 8, imagePath: `${process.env.PUBLIC_URL}/images/linear.png`, path: "/graphs7", footerName: "Data Normalization" },
  ];

  const dbFilePath = `${process.env.PUBLIC_URL}/priaData.db`;

  return (
    <>
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
        <a href={dbFilePath} download className="downloadLink">
          Download Database File
        </a>
      </div>
    </div>

    <div className="textBoxesContainer">
        <div className="textBox">
          <h2>Update</h2>
          <h4>Here is what's new today..</h4>
          <p>- Temperature has gone up 4 degrees</p>
          <p>- Humidity is down by 2%</p>
        </div>
        <div className="textBox">
          <h2>Suggestions</h2>
          <h4>Here are some suggestions..</h4>
          <p>- Since the temperature is higher today, try watering your plants a little extra to make up for the hotter weather</p>
          <p>- With the humidity being lower, mist your plants with water to help add moisture to the air and soil</p>
        </div>
      </div>
    </>
  );
};

export default HomePage;



