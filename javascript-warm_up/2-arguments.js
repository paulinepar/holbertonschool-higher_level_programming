#!/usr/bin/node
/*
declare variable process argv
slice(2) for start until of the third argument
*/
const args = process.argv.slice(2);
// if arg is 0
if (args.length === 0) {
  console.log('No argument');
// if arg is 1
} else if (args.length === 1) {
  console.log('Argument found');
// if arg is 2 or >
} else {
  console.log('Arguments found');
}
