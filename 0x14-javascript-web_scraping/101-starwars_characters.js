#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    //for (const i in charac) {
    //  request(charac[i].replace(/["\[\]]/g, ''), function (error, response, body) {
    //    if (error) {
    //      console.log(error);
    //    } else {
    //     const test = JSON.stringify(JSON.parse(body).name);
    //      console.log(test);
    //    }
    //  });
    //}
  }
});
