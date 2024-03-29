import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from './ThemeContext';
import Navbar from './NavBar';
import HomePage from './HomePage';
import AboutPage from './AboutPage';
import GraphsPage from './GraphsPage';
import SettingsPage from './SettingsPage';
import ChooseYourPlantPage from './ChooseYourPlantPage';
<<<<<<< HEAD
// import LoginPage from './LoginPage';
=======
import SimulationForm from './SimulationForm';
>>>>>>> 436ca1800301e2b8629b8aaec97ca7cc8ff35420

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    // Check if user is authenticated, e.g., by checking localStorage or cookies
    // For demonstration, assume isAuthenticated is stored in localStorage
    const storedAuth = localStorage.getItem('isAuthenticated');
    if (storedAuth === 'true') {
      setIsAuthenticated(true);
    } else {
      setIsAuthenticated(false);
    }
  }, []);

  return (
    <ThemeProvider>
      <Router>
        <Navbar />
        <Routes>
        <Route path="/" element={<HomePage />} />
<<<<<<< HEAD
          <Route path="/About" element={<AboutPage />} />
          <Route path="/Graphs" element={<GraphsPage />} />
          <Route path="/Settings" element={<SettingsPage />} />
          <Route path="/ChooseYourPlant" element={<ChooseYourPlantPage />} />
          <Route path="/Home" element={<HomePage />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}
// <Route path="/Login" element={<LoginPage />} />
// <Route path="/" element={isAuthenticated ? <HomePage /> : <Navigate to="/Login" />} />
export default App;


=======
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
>>>>>>> 436ca1800301e2b8629b8aaec97ca7cc8ff35420
