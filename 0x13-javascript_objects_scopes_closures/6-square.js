#!/usr/bin/node

const Square5 = require('./5-square');
module.exports = class Square extends Square5 {
  charPrint (c) {
    let charIn = 'x';
    if (c) {
      charIn = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(charIn.repeat(this.width));
    }
  }
};
