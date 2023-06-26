const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(dropdown => {
  const dropdownContent = dropdown.querySelector('.dropdown-content');
  const dropdownContentInfo = dropdown.querySelector('.dropdown-content-info');

  dropdown.addEventListener('mouseenter', () => {
    dropdown.classList.add('hover');
  });

  dropdown.addEventListener('mouseleave', () => {
    dropdown.classList.remove('hover');
  });

  if (dropdownContent) {
    dropdownContent.addEventListener('mouseleave', () => {
      if (dropdown.matches(':hover')) {
        dropdown.classList.add('hover');
      } else {
        dropdown.classList.remove('hover');
      }
    });
  }

  if (dropdownContentInfo) {
    dropdownContentInfo.addEventListener('mouseleave', () => {
      if (dropdown.matches(':hover')) {
        dropdown.classList.add('hover');
      } else {
        dropdown.classList.remove('hover');
      }
    });
  }
});