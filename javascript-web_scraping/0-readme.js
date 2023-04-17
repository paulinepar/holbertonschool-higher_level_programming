#!/usr/bin/node

const fs = require('fs')
const file = process.agrv[2];
fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
    console.log(data);
    }
});