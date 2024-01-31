#!/usr/bin/node
// Script displays the status of a get request
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
