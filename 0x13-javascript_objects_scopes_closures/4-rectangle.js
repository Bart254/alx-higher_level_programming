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

  rotate () {
    const height = this.height;
    this.height = this.width;
    this.width = height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
