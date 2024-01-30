#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(body);
});
