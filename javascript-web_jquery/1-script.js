$(document).ready(function () {
  // Wait for the DOM content to be fully loaded

  const header = $('header');

  // Check if the <header> element is found

  if (header.length > 0) {
    // Update the text color to red (#FF0000)

    header.css('color', '#FF0000');
  } else {
    console.error('Error: <header> element not found');
  }
});
