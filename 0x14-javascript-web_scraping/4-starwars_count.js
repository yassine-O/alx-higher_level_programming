#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  let count = 0;
  const movies = JSON.parse(body).results;
  for (const movie of movies) {
    for (const c of movie.characters) {
      if (c.includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
