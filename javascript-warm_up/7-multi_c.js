#!/usr/bin/node
/*
Write a script that prints x times “C is fun”

Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use console.log(...) to print all output
You are not allowed to use var
You can use only two console.log
You must use a loop (while, for, etc.)
*/
const args = process.argv.slice(2);

if (args) {
  for (let count = 0; count < args; count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
