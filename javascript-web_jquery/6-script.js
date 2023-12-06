$(document).ready(function () {
  // Wait for the DOM content to be fully loaded
  $('#update_header').click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
