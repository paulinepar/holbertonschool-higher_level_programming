#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let NBR_OF_MOVIES = 0;

  for (const film of data.results) {
    if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      NBR_OF_MOVIES++;
    }
  }
  console.log(NBR_OF_MOVIES);
});
