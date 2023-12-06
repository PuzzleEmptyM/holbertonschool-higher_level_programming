#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesCount = filmsData.reduce((count, film) => {
      if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        return count + 1;
      }
      return count;
    }, 0);
    console.log(wedgeAntillesCount);
  }
});
