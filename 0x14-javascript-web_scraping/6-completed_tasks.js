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
      if (jsonObject[i].userId in dic) {
        if (jsonObject[i].completed) {
          dic[jsonObject[i].userId] = (dic[jsonObject[i].userId] || 0) + 1;
        }
      } else {
        dic[jsonObject[i].userId] = 0;
        if (jsonObject[i].completed) {
          dic[jsonObject[i].userId] = (dic[jsonObject[i].userId] || 0) + 1;
        }
      }
    }
    console.log(dic);
  }
});
