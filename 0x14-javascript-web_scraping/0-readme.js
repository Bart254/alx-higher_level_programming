#!/usr/bin/node
const filePath = process.argv[2];
const fs = require('fs');
fs.readFile(filePath, 'UTF-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
