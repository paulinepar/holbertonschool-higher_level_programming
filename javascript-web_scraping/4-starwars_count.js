#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let NBR_OF_MOVIES = 0;

  for (const film of data.results) {
    if (film.characters.includes('/api/people/18/')) {
      NBR_OF_MOVIES++;
    }
  }
  console.log(NBR_OF_MOVIES);
});
