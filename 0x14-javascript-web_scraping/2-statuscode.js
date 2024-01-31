#!/usr/bin/node
// Script displays the status of a get request
const request = require('request');
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
