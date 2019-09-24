#!/usr/bin/node
exports.converter = function converter (base) {
  return function (value) {
    return value.toString(base);
  };
};
