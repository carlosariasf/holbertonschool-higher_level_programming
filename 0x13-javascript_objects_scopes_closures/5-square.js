#!/usr/bin/node

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super();
    if (size > 0) {
      this.width = size;
      this.height = size;
    }
  }
};
