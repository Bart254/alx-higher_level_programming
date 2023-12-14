#!/usr/bin/node
'use strict';
let times = process.argv[2];
const message = 'C is fun';
if (isNaN(times)) {
  console.log('Missing number of occurences');
}
while (times > 0) {
  console.log(message);
  times--;
}
