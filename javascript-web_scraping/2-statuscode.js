#!/usr/bin/node

const fs = require('fs');
const url = process.argv[2];
fs.get(url, (response) => {
        console.log(`code: ${response.statusCode}`);
      }).on("error", (error) => {
        console.timeLog(error)
      });