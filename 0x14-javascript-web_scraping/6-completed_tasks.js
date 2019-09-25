#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonObject = JSON.parse(body);
    const dic = {};
    for (const i in jsonObject) {
      if (jsonObject[i].completed) {
        if (!(jsonObject[i].userId in dic)) {
          dic[jsonObject[i].userId] = 1;
        } else {
          dic[jsonObject[i].userId]++;
        }
      }
    }
    console.log(dic);
  }
});
