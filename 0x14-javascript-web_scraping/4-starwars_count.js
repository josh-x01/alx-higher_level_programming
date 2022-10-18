#!/usr/bin/node

require('request')('https://swapi-api.hbtn.io/api/films', (e, r, b) => {
  if (e) console.log(e);
  else {
    const nb = JSON.parse(b).results.filter((elem) => {
      return elem.characters.filter((url) => { return url.includes('18'); }).length;
    }).length;
    console.log(nb);
  }
});
