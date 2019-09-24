#!/usr/bin/node
let fs = require('fs');
try {
  let text = fs.readFileSync('./' + process.argv[2], 'utf8').toString().split('\n');
}
catch(error) {
  console.error(error);
}
