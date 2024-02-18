#!/usr/bin/node
// Returns the number of films ID 18 is in
const request = require('request');
const url = process.argv[2];
const id = 18;
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
      for (let i = 0; i < results[index].characters.length; i++) {
        if (results[index].characters[i].includes(id)) {
          nb++;
        }
      }
    }
    console.log(nb);
  }
});
