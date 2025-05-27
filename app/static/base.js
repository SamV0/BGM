document.addEventListener('DOMContentLoaded', function() {
  // Text input uppercase conversion
  const inputs = document.querySelectorAll('input[type="text"], input[type="email"], textarea');
  inputs.forEach(input => {
    input.addEventListener('input', function() {
      if (this.value === this.value.toLowerCase() && this.value.length > 0) {
        this.value = this.value.toUpperCase();
      }
    });
  });

  // Theme switching functionality
  const themeToggle = document.getElementById('theme-toggle');
  const baseCss = document.getElementById('theme-css');
  const lightThemeCss = document.getElementById('light-theme-css');
  
  function setTheme(theme) {
    if (theme === 'light') {
      document.body.classList.add('light-theme');
      baseCss.disabled = true;
      lightThemeCss.disabled = false;
      themeToggle.textContent = '🌕';
    } else {
      document.body.classList.remove('light-theme');
      baseCss.disabled = false;
      lightThemeCss.disabled = true;
      themeToggle.textContent = '☀️';
    }
    localStorage.setItem('theme', theme);
  }

  // Load saved theme preference
  const currentTheme = localStorage.getItem('theme') || 'dark';
  setTheme(currentTheme);

  // Handle theme toggle
  themeToggle.addEventListener('click', function() {
    const newTheme = lightThemeCss.disabled ? 'light' : 'dark';
    setTheme(newTheme);
  });
});