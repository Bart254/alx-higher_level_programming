#!/usr/bin/node
const size = parseInt(process.argv[2]);
let square = '';
if (isNaN(size)) {
  console.log('Missing size');
}
for (let row = size; row > 0; row--) {
  for (let column = size; column > 0; column--) {
    square += 'X';
  }
  console.log(square);
  square = '';
}
