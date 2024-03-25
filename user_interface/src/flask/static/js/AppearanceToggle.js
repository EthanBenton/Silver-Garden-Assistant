// script.js
document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('themeToggle');
    const modeHeader = document.getElementById('modeHeader');
    const modeText = document.getElementById('modeText');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme) {
        document.body.classList.add(currentTheme);
        if (currentTheme === 'dark-mode') {
            themeToggle.checked = true;
            modeText.innerText = 'Dark Mode';
        } else {
            modeText.innerText = 'Light Mode';
        }
        updateHeaderColor(currentTheme); // Update header color based on the initial theme
    }

    themeToggle.addEventListener('change', function () {
        const newTheme = themeToggle.checked ? 'dark-mode' : 'light-mode';
        localStorage.setItem('theme', newTheme);
        document.body.classList.toggle('dark-mode', themeToggle.checked);
        modeText.innerText = themeToggle.checked ? 'Dark Mode' : 'Light Mode';
        updateHeaderColor(newTheme); // Update header color based on the new theme
    });

    function updateHeaderColor(theme) {
        modeHeader.style.color = theme === 'dark-mode' ? '#fff' : '#000';
    }
});





