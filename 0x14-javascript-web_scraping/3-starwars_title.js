#!/usr/bin/node

require('request')('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (e, r, b) => {
  if (e) console.log(e);
  else console.log(JSON.parse(b).title);
});
