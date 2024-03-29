import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './ThemeContext';
import Navbar from './NavBar';
import HomePage from './HomePage';
import AboutPage from './AboutPage';
import GraphsPage from './GraphsPage';
import SettingsPage from './SettingsPage';
import ChooseYourPlantPage from './ChooseYourPlantPage';
import SimulationForm from './SimulationForm';

function App() {
  return (
    <ThemeProvider> {}
    <Router>
      <Navbar /> {}
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/About" element={<AboutPage />} />
        <Route path="/graphs" element={<GraphsPage />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/ChooseYourPlant" element={<ChooseYourPlantPage />} />
        <Route path="/SimulationForm" element={<SimulationForm/>} />
      </Routes>
    </Router>
    </ThemeProvider>
  );
}

export default App;