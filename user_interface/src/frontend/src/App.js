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
import GraphsPage4 from './GraphsPage4';
import GraphsPage5 from './GraphsPage5';
import GraphsPage6 from './GraphsPage6';
import GraphsPage7 from './GraphsPage7';
import SettingsPage from './SettingsPage';
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
        <Route path="/graphs4" element={<GraphsPage4 />} />
        <Route path="/graphs5" element={<GraphsPage5 />} />
        <Route path="/graphs6" element={<GraphsPage6 />} />
        <Route path="/graphs7" element={<GraphsPage7 />} />
        <Route path="/settings" element={<SettingsPage />} />
        <Route path="/ChooseYourPlant" element={<ChooseYourPlantPage />} />
        <Route path="/SimulationForm" element={<SimulationForm/>} />
      </Routes>
    </Router>
    </ThemeProvider>
  );
}

export default App;