#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response.statusCode);
});
