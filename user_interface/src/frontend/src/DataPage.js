import React from 'react';
import { Link } from 'react-router-dom';
import styles from './DataPage.css';


/**
 * DataPage display the data page content
 */
const DataPage = () => {

  // Data for boxes with images and links with text ontop
  const boxes = [
    { id: 1, imagePath: `${process.env.PUBLIC_URL}/images/dotgraph.png`, path: "/graphs0", footerName: "Simulated Data Visualization" },
    { id: 2, imagePath: `${process.env.PUBLIC_URL}/images/TableGraph.png`, path: "/graphs1", footerName: "Data in Tables" },
    { id: 3, imagePath: `${process.env.PUBLIC_URL}/images/watering.png`, path: "/graphs2", footerName: "Watering Schedule" },
    { id: 4, imagePath: `${process.env.PUBLIC_URL}/images/linear.png`, path: "/graphs3", footerName: "Regression Model" },
  ];

   const dbFilePath = `${process.env.PUBLIC_URL}../../../../data_processing_visualization/database/priaData.db`;

  return (
    <>

    <div className="containerStyle">

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

    <a href={dbFilePath} download className="downloadLink">
      Download Database File
    </a>

    </>
  );
};

export default DataPage;



