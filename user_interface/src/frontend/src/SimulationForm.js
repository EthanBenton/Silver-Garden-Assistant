import React, { useState } from 'react';

const SimulationForm = () => {
  const [formData, setFormData] = useState({
    num_samples: 100,
    temp_start: 0,
    temp_end: 50,
    humidity_start: 0,
    humidity_end: 100,
    polling_rate_seconds: 10,
    noise_mean: 0.0,
    noise_std: 1.0,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      // Handle the simulated data response
      console.log(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Number of Samples:
        <input
          type="number"
          name="num_samples"
          value={formData.num_samples}
          onChange={handleChange}
        />
      </label>
      <label>
        Temperature Start Range:
        <input
          type="number"
          name="temp_start"
          value={formData.temp_start}
          onChange={handleChange}
          step="0.1"
        />
      </label>
      {/* Add more form inputs for other parameters */}
      <button type="submit">Generate Data</button>
    </form>
  );
};

export default SimulationForm;