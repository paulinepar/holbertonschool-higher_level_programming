#!/usr/bin/node

/*
Write a script that prints the addition of 2 integers
*/

const argv = process.argv;

const a = argv[2];
const b = argv[3];

function add (a, b) {
  if (a && b) {
    console.log(Number(a) + Number(b));
  } else {
    console.log('NaN');
  }
}
add(a, b);
