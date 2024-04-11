import React from 'react';
import { useTheme } from './ThemeContext';
const SettingsPage = () => {
  const { theme, toggleTheme } = useTheme();

  return (
    <div style={{ background: theme === 'dark' ? '#333' : '#FFF', color: theme === 'dark' ? '#FFF' : '#333' }}>
      <h1>Settings</h1>
      <label>
        Dark Mode
        <input
          type="checkbox"
          checked={theme === 'dark'}
          onChange={toggleTheme}
        />
      </label>
    </div>
  );
};

export default SettingsPage;

