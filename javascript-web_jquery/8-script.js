$(document).ready(function () {
    // Wait for the DOM content to be fully loaded
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
      // Extract the list of movies from the response data
      const movies = data.results;
  
      // Iterate over each movie and append its title to the UL#list_movies
      for (const movie of movies) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      }
    });
  });
