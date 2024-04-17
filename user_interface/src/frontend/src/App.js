import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './ThemeContext';
//Linking files to words
import Navbar from './NavBar';
import HomePage from './HomePage';
import AboutPage from './AboutPage';
import GraphsPage0 from './GraphsPage0';
import GraphsPage1 from './GraphsPage1';
import GraphsPage2 from './GraphsPage2';
import GraphsPage3 from './GraphsPage3';
import SettingsPage from './SettingsPage';
import DataPage from './DataPage';
import ChooseYourPlantPage from './ChooseYourPlantPage';
import SimulationForm from './SimulationForm';

function App() {
  return (
    // ThemeProvider to manage the theme of the application
    <ThemeProvider> {}
    <Router>
      {/* Navbar for navigation */}
      <Navbar /> {}
      {/* Routes for different pages */}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/About" element={<AboutPage />} />
        <Route path="/graphs0" element={<GraphsPage0 />} />
        <Route path="/graphs1" element={<GraphsPage1 />} />
        <Route path="/graphs2" element={<GraphsPage2 />} />
        <Route path="/graphs3" element={<GraphsPage3 />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/Data" element={<DataPage />} />
        <Route path="/ChooseYourPlant" element={<ChooseYourPlantPage />} />
        <Route path="/SimulationForm" element={<SimulationForm/>} />
      </Routes>
    </Router>
    </ThemeProvider>
  );
}

export default App;