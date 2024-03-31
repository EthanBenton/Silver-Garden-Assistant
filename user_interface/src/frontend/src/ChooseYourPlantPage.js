import React, { useState } from 'react';
import './ChooseYourPlantPage.css'; 

const plantImages = {
  rose: `${process.env.PUBLIC_URL}/images/rose.png`,
  tulip: `${process.env.PUBLIC_URL}/tulip.png`,//place holder
  // Add more plants as needed
};

const ChooseYourPlantPage = () => {
  const [plants, setPlants] = useState([]);
  const [plantInput, setPlantInput] = useState('');

  const addPlant = () => {
    const plantName = plantInput.toLowerCase();
    if (plantName && !plants.includes(plantName)) {
      setPlants((prevPlants) => [...prevPlants, plantName]);
      setPlantInput('');
    }
  };

  const removePlant = (plantToRemove) => {
    setPlants((prevPlants) => prevPlants.filter(plant => plant !== plantToRemove));
  };

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
        <button onClick={addPlant} className="addPlantButton">
          Add Plant
        </button>
      </div>
      <ul className="plantList">
        {plants.map((plant, index) => (
          <li key={index} className="plantItem">
            {capitalizeFirstLetter(plant)}
            {plantImages[plant] ? (
              <img 
                src={plantImages[plant]} 
                alt={plant} 
                className="plantImage"
              />
            ) : null}
            <button 
              onClick={() => removePlant(plant)} 
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








