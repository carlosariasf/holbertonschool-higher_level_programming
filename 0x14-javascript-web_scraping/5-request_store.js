#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.appendFile(process.argv[3], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
