#!/usr/bin/node

//  Write a script that prints a square

const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
