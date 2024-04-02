import React, { useState, useEffect } from 'react';
import './ChooseYourPlantPage.css';

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

const ChooseYourPlantPage = () => {
  const [plants, setPlants] = useState(() => {
    const savedPlants = localStorage.getItem('plants');
    return savedPlants ? JSON.parse(savedPlants) : [];
  });
  const [plantInput, setPlantInput] = useState('');

  useEffect(() => {
    localStorage.setItem('plants', JSON.stringify(plants));
  }, [plants]);

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

  const removePlant = (plantKeyToRemove) => {
    setPlants(prevPlants => prevPlants.filter(plant => plant.key !== plantKeyToRemove));
  };

  const capitalizeFirstLetter = (string) => {
    if (!string) return '';
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  

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
        <button onClick={addPlant} className="addPlantButton">
          Add Plant
        </button>
      </div>
      <ul className="plantList">
        {plants.map((plant, index) => (
          <li key={index} className="plantItem">
            {capitalizeFirstLetter(plant.name)}
            {plantImages[plant.key] ? (
              <img 
                src={plantImages[plant.key]} 
                alt={plant.name} 
                className="plantImage"
              />
            ) : null}
            <button 
              onClick={() => removePlant(plant.key)}
              className="removePlantButton">
              X
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChooseYourPlantPage;
