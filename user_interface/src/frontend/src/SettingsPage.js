import React from 'react';
import { useTheme } from './ThemeContext';

/**
 * SettingsPage component for displaying settings
 */
const SettingsPage = () => {

  // Theme and toggleTheme function from ThemeContext
  const { theme, toggleTheme } = useTheme();

  // Determine the theme based on the current theme
  const themeClass = theme === 'dark' ? 'darkTheme' : 'lightTheme';

  return (
    <div className={themeClass}>
      <h1>Settings</h1>
      <label>
        Dark Mode
        <input
          type="checkbox"
          checked={theme === 'dark'} // Set the checkbox checked state based on the current theme
          onChange={toggleTheme} // Call toggleTheme function when the checkbox changes
        />
      </label>
    </div>
  );
};

export default SettingsPage;

