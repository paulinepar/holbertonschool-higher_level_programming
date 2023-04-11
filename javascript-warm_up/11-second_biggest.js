#!/usr/bin/node
/*
Write a script that searches the second biggest integer in the list of arguments.
You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var
*/

// ... : convert arguments in array
const nums = [...process.argv.slice(2)]
// filter : filter if the numbers is not numbers to check if isNaN return false
  .filter(arg => !isNaN(arg))
  .sort((a, b) => b - a)[1] || 0;

console.log(nums);
