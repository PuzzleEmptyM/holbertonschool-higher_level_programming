$(document).ready(function () {
    // Wait for the DOM content to be fully loaded
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
      // Update the text of the <div id="character"> element with the character name
      $('#character').text(data.name);
    });
  });
