#!/usr/bin/node
// Returns the number of films ID 18 is in
const request = require('request');
const url = process.argv[2];
const id = 18;
const user = 'https://swapi-api.alx-tools.com/api/people/' + id + '/';
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    let data = body;
    if (typeof body === 'string') {
      data = JSON.parse(body);
    }
    const results = data.results;
    let nb = 0;
    for (let index = 0; index < data.count; index++) {
      if (results[index].characters.includes(user)) {
        nb++;
      }
    }
    console.log(nb);
  }
});
