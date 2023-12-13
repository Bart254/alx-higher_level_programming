#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rec = '';
    for (let row = this.height; row > 0; row--) {
      for (let col = this.width; col > 0; col--) {
        rec += 'X';
      }
      console.log(rec);
      rec = '';
    }
  }
}
module.exports = Rectangle;
