#!/usr/bin/node
// Get the names of characters in a film
const request = require('request');
const id = process.argv[2];
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
request.get(filmUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    let results = body;
    if (typeof body === 'string') {
      results = JSON.parse(body);
    }
    for (let index = 0; index < results.characters.length; index++) {
      const userUrl = results.characters[index];
      request.get(userUrl, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          let userResults = body;
          if (typeof body === 'string') {
            userResults = JSON.parse(body);
          }
          console.log(userResults.name);
        }
      });
    }
  }
});
