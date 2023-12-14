#!/usr/bin/node
const prototype = require('./5-square');

class Square extends prototype {
  constructor (size) {
    super(size);
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
