#!/usr/bin/node

/*
Write a script that computes and prints a factorial
The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var
*/
const nbr = parseInt(process.argv[2])

function fact (nbr) {
  if (nbr === 0 || isNaN(nbr)) {
    return 1;
  } else {
    return nbr * fact(nbr - 1);
  }
}
console.log(fact(nbr));
