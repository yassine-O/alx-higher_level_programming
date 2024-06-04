#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('node:fs');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(filename, body, err => {
    if (err) {
      console.error(err);
    }
  });
});
