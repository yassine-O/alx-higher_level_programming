#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const movie = JSON.parse(body);
  let i = 0;
  while (i < movie.characters.length) {
    request(movie.characters[i], function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
    i++;
  }
});
