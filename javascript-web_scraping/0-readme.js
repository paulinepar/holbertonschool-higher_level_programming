#!/usr/bin/node

const fs = require('fs')
fs.readfile('file', 'utf8', (err, inputD) => {
    if (err) {
        console.log(err);
    } else {
    console.log(inputD.toString());
    }
})