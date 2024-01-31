#!/usr/bin/node
// stores the content of a website in a file
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    let content = body;
    if (typeof body === 'object') {
      content = JSON.stringify(body);
    }
    fs.writeFile(filePath, content, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
