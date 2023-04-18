#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const nbMovies = JSON.parse(body).results.filter((film) => {
    return film.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(nbMovies);
});
