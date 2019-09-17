#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(parseInt(process.argv[2]));
} else {
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}
function add (a, b) {
  console.log(a + b);
}
