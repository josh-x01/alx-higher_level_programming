#!/usr/bin/node

require('request')(process.argv[2], (e, r, b) => {
  require('fs').writeFile(process.argv[3], b, e => { if (e) console.log(e); });
});
