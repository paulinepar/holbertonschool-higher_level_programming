#!/usr/bin/node
// declare variable process argv
const args = process.argv;
// if arg
if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
