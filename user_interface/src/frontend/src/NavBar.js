import React from 'react';
import { Link } from 'react-router-dom';
import { useTheme } from './ThemeContext'; // Ensure the path matches where your ThemeContext file is located
import './NavBar.css'; // Import the CSS for styling

const NavBar = () => {
  const { theme } = useTheme(); // Access the current theme

  return (
    <nav className={`navbar ${theme}`}>
      <Link to="/settings" className="nav-link">Settings</Link>
      <Link to="/" className="nav-link">Home</Link>
      <Link to="/About" className="nav-link">About</Link>
      <Link to="/graphs" className="nav-link">Graphs</Link>
      <Link to="/ChooseYourPlant" className="nav-link">Choose Your Plant</Link>
      <Link to="/SimulationForm" className="nav-link">Simulate</Link>
    </nav>
  );
};

export default NavBar;



