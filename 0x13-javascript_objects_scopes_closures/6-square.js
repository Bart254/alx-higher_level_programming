#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let square = '';
    if (!c) {
      c = 'X';
    }
    for (let row = 1; row <= this.height; row++) {
      for (let col = 1; col <= this.width; col++) {
        square += c;
      }
      console.log(square);
      square = '';
    }
  }
}
module.exports = Square;
