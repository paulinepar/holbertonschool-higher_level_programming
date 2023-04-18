#!/usr/bin/node

const request = require('request');
const id = '18';
const url = 'https://swapi-api.hbtn.io/api/films/'
const character = `https://swapi-api.hbtn.io/api/people/${id}/`
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let nbr_of_movies = 0;

  for (let film of data.results) {
    if (film.characters.includes(character)) {
      nbr_of_movies++;
    }
  }
  console.log(nbr_of_movies);
});
