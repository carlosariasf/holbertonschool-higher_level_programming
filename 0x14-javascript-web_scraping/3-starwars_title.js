#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonObject = JSON.parse(body);
    console.log(jsonObject.title);
  }
});
