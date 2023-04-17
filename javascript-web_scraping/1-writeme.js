#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];
fs.writeFile(file, data, 'utf8', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
