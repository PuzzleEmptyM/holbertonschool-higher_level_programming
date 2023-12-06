$(document).ready(function () {
    // Wait for the DOM content to be fully loaded
    $('#toggle_header').click(function () {
      // Toggle the class 'red' and 'green' on the <header> element
      $('header').toggleClass('red green');
    });
  });
