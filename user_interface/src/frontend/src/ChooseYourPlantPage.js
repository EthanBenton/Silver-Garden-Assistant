import React, { useState, useEffect } from 'react';
import './ChooseYourPlantPage.css';


/**
 * Stores the paths for the converted inputs
 */
const plantImages = {
  rose: `${process.env.PUBLIC_URL}/images/PlantDB/rose.png`,
  greenpepper: `${process.env.PUBLIC_URL}/images/PlantDB/greenpepper.png`,
  watermelon: `${process.env.PUBLIC_URL}/images/PlantDB/watermelon.png`,
  tomato: `${process.env.PUBLIC_URL}/images/PlantDB/tomato.png`,
  redpepper: `${process.env.PUBLIC_URL}/images/PlantDB/redpepper.png`,
  yellowpepper: `${process.env.PUBLIC_URL}/images/PlantDB/yellowpepper.png`,
  carrot: `${process.env.PUBLIC_URL}/images/PlantDB/carrot.png`,
  cucumber: `${process.env.PUBLIC_URL}/images/PlantDB/cucumber.png`,
  squash: `${process.env.PUBLIC_URL}/images/PlantDB/squash.png`,
  zucchini: `${process.env.PUBLIC_URL}/images/PlantDB/zucchini.png`,
  lettuce: `${process.env.PUBLIC_URL}/images/PlantDB/lettuce.png`,
  potato: `${process.env.PUBLIC_URL}/images/PlantDB/potato.png`,
  // Add more plants as needed
};

/**
 * Stores the descriptions of the plants
 */
const plantDetails = {
  rose: "Roses have thorns.",
  greenpepper: "Green peppers are good in spagetti.",
  watermelon: "Watermelons are mostly of water.",
  tomato: "Tomatoes are good on pizza.",
  redpepper: "Red pepper are good with ranch.",
  yellowpepper: "Yellow peppers are good with ranch too.",
  carrot: "Carrots are underground.",
  cucumber: "These are pickles I think.",
  squash: "Is gross.",
  zucchini: "Gross x2.",
  lettuce: "Good on a salad.",
  potato: "Are very versatile.",
  // Add more as needed
};

/**
 * Component for choosing plants to add or remove from the garden.
 * @returns JSX element
 */
const ChooseYourPlantPage = () => {
  const [plants, setPlants] = useState(() => {
    const savedPlants = localStorage.getItem('plants');
    return savedPlants ? JSON.parse(savedPlants) : [];
  });
  const [plantInput, setPlantInput] = useState('');
  const [selectedPlant, setSelectedPlant] = useState(null);

  // Save plants to local storage
  useEffect(() => {
    localStorage.setItem('plants', JSON.stringify(plants));
  }, [plants]);

  /**
   * Function to add a new plant to the list
   */
  const addPlant = () => {
    const plantName = plantInput.toLowerCase();
    const plantKey = plantInput.replace(/\s+/g, '').toLowerCase();
    
    if (plantKey && !plants.some(plant => plant.key === plantKey)) {
      setPlants(prevPlants => [
        ...prevPlants, 
        { key: plantKey, name: plantName }
      ]);
      setPlantInput('');
    }
  };

  /**
   * Function to remove a plant from the list
   */
  const removePlant = (event, plantKeyToRemove) => {
    event.stopPropagation();
    setPlants(prevPlants => prevPlants.filter(plant => plant.key !== plantKeyToRemove));
  };

  /**
   * Function to handle selecting a plant for details
   */
  const handleSelectPlant = (plant) => {
    if (!plantImages[plant.key]) return; // Only make clickable if image exists
    setSelectedPlant(plant);
  };

  /**
   * Function to close the popup with plant details
   */
  const closePopup = () => {
    setSelectedPlant(null);
  };

  /**
   * Function to capitalize the first letter of a string
   */
  const capitalizeFirstLetter = (string) => string.charAt(0).toUpperCase() + string.slice(1);

  return (
    <div className="choosePlantContainer">
      <div className="choosePlantHeader">
        <h1>Choose Your Plant</h1>
        <p>Select plants to add or remove from your garden.</p>
        <input
          type="text"
          value={plantInput}
          onChange={(e) => setPlantInput(e.target.value)}
          placeholder="Type a plant name"
          className="plantInput"
        />
        <button onClick={addPlant} className="addPlantButton">Add Plant</button>
      </div>
      <div className="plantsDisplayBox">
        <ul className="plantList">
          {/* List of plants */}
          {plants.map((plant, index) => (
            <li key={index} className={`plantItem ${!plantImages[plant.key] ? 'nonClickable' : ''}`} onClick={() => handleSelectPlant(plant)}>
              {capitalizeFirstLetter(plant.name)}
              {plantImages[plant.key] && <img src={plantImages[plant.key]} alt={plant.name} className="plantImage" />}
              <button onClick={(event) => removePlant(event, plant.key)} className="removePlantButton">X</button>
            </li>
          ))}
        </ul>
      </div>
      {/* Popup for displaying plant details */}
      {selectedPlant && (
        <div className="plantDetailsPopup">
          <div className="popupContent">
            <h2>{capitalizeFirstLetter(selectedPlant.name)}</h2>
            <p>{plantDetails[selectedPlant.key] || "No additional information available."}</p>
            <button onClick={closePopup}>Close</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChooseYourPlantPage;