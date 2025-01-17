// Immediately apply dark mode if stored in localStorage
document.addEventListener("DOMContentLoaded", () => {
    const savedMode = localStorage.getItem('theme');
    const body = document.body;
    const modeIcon = document.getElementById('mode-icon');
  
    if (savedMode === 'dark') {
      body.classList.add('dark-mode');
      if (modeIcon) {
        modeIcon.classList.remove('fa-moon');
        modeIcon.classList.add('fa-sun');
      }
    }
  });
  
  // Toggle dark mode and save the preference
  document.getElementById('toggle-dark-mode')?.addEventListener('click', () => {
    const body = document.body;
    const modeIcon = document.getElementById('mode-icon');
    
    body.classList.toggle('dark-mode');
    
    if (body.classList.contains('dark-mode')) {
      modeIcon.classList.remove('fa-moon');
      modeIcon.classList.add('fa-sun');
      localStorage.setItem('theme', 'dark'); // Save "dark" mode in localStorage
    } else {
      modeIcon.classList.remove('fa-sun');
      modeIcon.classList.add('fa-moon');
      localStorage.setItem('theme', 'light'); // Save "light" mode in localStorage
    }
  });