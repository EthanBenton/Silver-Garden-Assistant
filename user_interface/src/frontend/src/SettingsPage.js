import React from 'react';
import { useTheme } from './ThemeContext';
import styles from './SettingsPage.css';

/**
 * SettingsPage component for displaying settings
 */
const SettingsPage = () => {

  // Theme and toggleTheme function from ThemeContext
  const { theme, toggleTheme } = useTheme();

  // Determine the theme based on the current theme
  const themeClass = theme === 'dark' ? 'darkTheme' : 'lightTheme';

  return (
    <div className={`settingsContainer ${themeClass}`}>
      <label className="toggleLabel">
        <h1>Dark Mode</h1>
        <div className="toggleSwitch">
          <input
            type="checkbox"
            checked={theme === 'dark'}
            onChange={toggleTheme}
          />
          <span className="slider"></span>
        </div>
      </label>
    </div>
  );
};

export default SettingsPage;

