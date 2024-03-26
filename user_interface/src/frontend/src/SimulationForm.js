import React, { useState } from 'react';
import Slider from 'rc-slider';
import 'rc-slider/assets/index.css';
import './SimulationForm.css';
import Select from 'react-select';

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
    const value = e.target.name === 'noise_mean' || e.target.name === 'noise_std' 
      ? parseFloat(e.target.value) 
      : e.target.value;
    setFormData({ ...formData, [e.target.name]: value });
  };

  const handleSliderChange = (name, value) => {
    if (name === 'temp_start') {
      setFormData({ ...formData, temp_start: value[0], temp_end: value[1] });
    } else if (name === 'temp_end') {
      setFormData({ ...formData, temp_end: value[1] });
    } else if (name === 'humidity_start') {
      setFormData({ ...formData, humidity_start: value[0], humidity_end: value[1] });
    } else if (name === 'humidity_end') {
      setFormData({ ...formData, humidity_end: value[1] });
    }
  };
  const handleDropdownChange = (name, selectedOption) => {
    setFormData({ ...formData, [name]: selectedOption.value });
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
      console.log(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const pollingRateOptions = [
    { value: 5, label: '5 seconds' },
    { value: 10, label: '10 seconds' },
    { value: 15, label: '15 seconds' },
    { value: 20, label: '20 seconds' },
  ];

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
        Temperature Range:
        <Slider
          range
          min={0}
          max={50}
          value={[formData.temp_start, formData.temp_end]}
          onChange={(value) => handleSliderChange('temp_start', value)}
        />
        <div>
          Start: {formData.temp_start} &deg;C, End: {formData.temp_end} &deg;C
        </div>
      </label>
      <label>
        Humidity Range:
        <Slider
          range
          min={0}
          max={100}
          value={[formData.humidity_start, formData.humidity_end]}
          onChange={(value) => handleSliderChange('humidity_start', value)}
        />
        <div>
          Start: {formData.humidity_start}%, End: {formData.humidity_end}%
        </div>
      </label>
      <label>
        Polling Rate:
        <Select
          options={pollingRateOptions}
          value={pollingRateOptions.find((option) => option.value === formData.polling_rate_seconds)}
          onChange={(selectedOption) => handleDropdownChange('polling_rate_seconds', selectedOption)}
        />
      </label>
      <label>
        Noise Mean:
        <input
          type="number"
          name="noise_mean"
          value={formData.noise_mean}
          onChange={handleChange}
        />
      </label>
      <label>
        Noise Standard Deviation:
        <input
          type="number"
          name="noise_std"
          value={formData.noise_std}
          onChange={handleChange}
        />
      </label>
      <button type="submit">Generate Data</button>
    </form>
  );
};

export default SimulationForm;