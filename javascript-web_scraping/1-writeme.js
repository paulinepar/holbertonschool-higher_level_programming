#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const file = argv[2];
const data = argv[3];
fs.writeFile(file, data, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
