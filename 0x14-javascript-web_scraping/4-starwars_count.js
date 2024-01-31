#!/usr/bin/node
// Returns the number of films ID 18 is in
const request = require('request');
const url = process.argv[2];
const user = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const body = JSON.parse(response.body);
    const results = body.results; let nb = 0;
    for (let index = 0; index < body.count; index++) {
      if (results[index].characters.includes(user)) {
        nb++;
      }
    }
    console.log(nb);
  }
});
