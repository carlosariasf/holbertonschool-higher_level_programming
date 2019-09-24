#!/usr/bin/node
const fs = require('fs');
try {
  console.log((fs.readFileSync('./' + process.argv[2], 'utf8').split('\n')[0]));
} catch (error) {
  console.error(error);
}
