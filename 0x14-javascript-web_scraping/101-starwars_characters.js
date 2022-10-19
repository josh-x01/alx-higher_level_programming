#!/usr/bin/node

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (e, r, b) => {
  if (e) console.log(e);
  JSON.parse(b).characters.forEach(url => {
    request(url, (err, response, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  });
});
