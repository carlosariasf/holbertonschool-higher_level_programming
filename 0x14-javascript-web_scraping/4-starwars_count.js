#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonObject = JSON.parse(body).results;
    let count = 0;
    for (const i in jsonObject) {
      for (const j in jsonObject[i].characters) {
        if (jsonObject[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
