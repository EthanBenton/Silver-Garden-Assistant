import React, { useState } from 'react';

const plantImages = {
  rose: `${process.env.PUBLIC_URL}/rose.png`,
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
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '20px' }}>
      <div style={{ textAlign: 'center' }}>
        <h1 style={{ fontSize: '3rem' }}>Choose Your Plant</h1>
        <p style={{ fontSize: '1.5rem' }}>Select plants to add or remove from your garden.</p>
        <input
          type="text"
          value={plantInput}
          onChange={(e) => setPlantInput(e.target.value)}
          placeholder="Type a plant name"
          style={{ fontSize: '1.5rem', padding: '10px', margin: '10px 0' }}
        />
        <button 
          onClick={addPlant} 
          style={{ fontSize: '1.5rem', padding: '10px 20px' }}>
          Add Plant
        </button>
      </div>
      <ul style={{ alignSelf: 'flex-start', width: '100%', paddingLeft: '20px' }}>
        {plants.map((plant, index) => (
          <li key={index} style={{ fontSize: '1.5rem', marginBottom: '10px' }}>
            {capitalizeFirstLetter(plant)}
            {plantImages[plant] ? (
              <img 
                src={plantImages[plant]} 
                alt={plant} 
                style={{ width: '300px', height: '300px', marginLeft: '20px', verticalAlign: 'middle' }}
              />
            ) : null}
            <button 
              onClick={() => removePlant(plant)} 
              style={{ fontSize: '1.5rem', marginLeft: '20px' }}>
              X
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChooseYourPlantPage;







