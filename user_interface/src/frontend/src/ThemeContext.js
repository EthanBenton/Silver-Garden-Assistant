import React, { createContext, useContext, useState, useEffect } from 'react';

const ThemeContext = createContext();

// access the theme context
export const useTheme = () => useContext(ThemeContext);

// Manages the theme state and provides it to the children components
export const ThemeProvider = ({ children }) => {
  
  /**
   * Keep the current theme ('light' or 'dark'), default is 'light'
   */ 
  const [theme, setTheme] = useState('light'); 

  /**
   * Apply the theme class to the body element whenever the theme changes
   */ 
  useEffect(() => {
    
    document.body.className = theme; // Apply the theme class to the body
  }, [theme]); // runs whenever the theme state changes

  /**
   * Function to toggle between light and dark themes
   */  
  const toggleTheme = () => {
    
    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light')); // Update the theme state based on the previous theme
  };

   /**
   * Provide the theme state and toggle function to the children components using the ThemeContext
   */ 
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};



