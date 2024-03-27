import React from 'react';
import { Link } from 'react-router-dom';
import { useTheme } from './ThemeContext'; // Import useTheme from your ThemeContext file

const Navbar = () => {
  const { theme } = useTheme(); // Access the current theme

  // Adjust styles based on the theme
  const navStyle = {
    backgroundColor: theme === 'dark' ? '#333' : '#f8f9fa', // Dark or light background
    color: theme === 'dark' ? 'white' : '#212529', // Dark or light text
    padding: '10px',
  };

  const linkStyle = {
    color: theme === 'dark' ? 'white' : '#212529', // Dark or light link text
    textDecoration: 'none',
    margin: '0 10px',
  };

  return (
    <nav style={navStyle}>
      <Link to="/settings" style={linkStyle}>Settings</Link>
      <Link to="/" style={linkStyle}>Home</Link>
      <Link to="/About" style={linkStyle}>About</Link>
      <Link to="/graphs" style={linkStyle}>Graphs</Link>
      <Link to="/ChooseYourPlant" style={linkStyle}>Choose Your Plant</Link>
      <Link to="/SimulationForm" style={linkStyle}>Simulate</Link>
    </nav>
  );
};

export default Navbar;


