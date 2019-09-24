#!/usr/bin/node
const list = require('./100-data');
console.log(list.list);
const nList = list.list.map((n, index) => n * index);
console.log(nList);
