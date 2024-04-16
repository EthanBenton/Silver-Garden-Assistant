import React, { useState } from 'react';
import Slider from 'rc-slider';
import 'rc-slider/assets/index.css';
import './SimulationForm.css';
import Select from 'react-dropdown-select';

const SimulationForm = () => {
  const [formData, setFormData] = useState({
    temp_start: 0,
    temp_end: 50,
    humidity_start: 0,
    humidity_end: 100,
    polling_rate_seconds: 10,
    noise_mean: 0.0,
    noise_std: 1.0,
    time_interval: 1,
    time_unit: 'seconds',
  });

  const handleChange = (e) => {
    let value;
    if (e.target.name === 'noise_mean' || e.target.name === 'noise_std') {
      value = parseFloat(e.target.value);
    } else if (e.target.name === 'polling_rate_seconds' ) {
      value = parseInt(e.target.value, 10);
    } else {
      value = e.target.value;
    }
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

  const handleDropdownChange = (selectedOption) => {
    if (selectedOption && selectedOption.length > 0) {
      const selectedValue = selectedOption[0].value;
      setFormData({ ...formData, time_unit: selectedValue });
    }
  };
  
  const handlePollingRateChange = (selectedOption) => {
    if (selectedOption && selectedOption.length > 0) {
      const selectedValue = selectedOption[0].value;
      setFormData({ ...formData, polling_rate_seconds: selectedValue });
    }
  };
  
  const timeUnitOptions = [
    { value: 'seconds', label: 'Seconds' },
    { value: 'minutes', label: 'Minutes' },
    { value: 'hours', label: 'Hours' },
    { value: 'days', label: 'Days' },
    { value: 'weeks', label: 'Weeks' },
    { value: 'months', label: 'Months' },
  ];

  const [simulatedData, setSimulatedData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send the form data to the /api/simulate endpoint
      const simulateResponse = await fetch('/api/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const simulatedData = await simulateResponse.json();
  
      if (simulateResponse.ok) {
        setSimulatedData(simulatedData); 
      } else {
        console.error('Error simulating data:', simulatedData.error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const generateJsonFile = (data) => {
    const dataStr = JSON.stringify(data, null, 2); 
    const blob = new Blob([dataStr], { type: 'application/json' }); 
    const url = URL.createObjectURL(blob); 
    const link = document.createElement('a'); 
    link.href = url; 
    link.download = 'simulated_data.json'; 
    link.click(); 
    URL.revokeObjectURL(url); 
  };

  const pollingRateOptions = [
    { value: 10, label: '10 seconds' },
    { value: 30, label: '30 seconds' },
    { value: 60, label: '1 minute' },
    { value: 300, label: '5 minutes' },
    { value: 600, label: '10 minutes' },
  ];


  /**
   * 
   * used to make an api call to the flask backend and displa
   */
  const handleGenerateGraph = async () => {
    try {
      if (simulatedData) {
        const graphResponse = await fetch('/api/graph0', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(simulatedData),
        });
        const graphData = await graphResponse.json();
  
        if (graphResponse.ok) {
          console.log('Graph generated successfully:', graphData.filePath);
      
        } else {
          console.error('Error generating graph:', graphData.error);
        }
      } else {
        console.error('No simulated data available. Please generate data first.');
      }
    } catch (error) {
      console.error('Error:', error.message);
      alert(`Error: ${error.message}`);
    }
  };

  return (
    <div>
    <form onSubmit={handleSubmit}>
    <div className="time-input-container">
        <label>
          Time Interval:
          <input
            type="number"
            name="time_interval"
            value={formData.time_interval}
            onChange={handleChange}
          />
        </label>
        <label>
        Time Unit:
        <Select
             options={timeUnitOptions}
             value={timeUnitOptions.find((option) => option.value === formData.time_unit)}
             onChange={handleDropdownChange}
          />
        </label>
      </div>
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
          onChange={(selectedOption) => handlePollingRateChange(selectedOption)}
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
    <button type="button" onClick={() => simulatedData && generateJsonFile(simulatedData)}>
       Download JSON File
    </button>
    <button onClick={handleGenerateGraph}>Generate Graph</button>
   </div>
    
  );



};

export default SimulationForm;