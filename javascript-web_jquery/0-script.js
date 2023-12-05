document.addEventListener('DOMContentLoaded', function () {
  // Wait for the DOM content to be fully loaded

  const header = document.querySelector('header');

  // Check if the <header> element is found

  if (header) {
    // Update the text color to red (#FF0000)

    header.style.color = '#FF0000';
  } else {
    console.error('Error: <header> element not found');
  }
});
