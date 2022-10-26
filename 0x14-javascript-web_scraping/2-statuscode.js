#!/usr/bin/node

require('request')(process.argv[2], (e, r) => {
  if (e) console.log(e);
  else console.log("code", r && r.statusCode);
});
