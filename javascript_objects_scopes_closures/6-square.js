#!/usr/bin/node
/*
Write a class Square that defines a square and inherits from Square of 5-square.js:
You must use the class notation for defining your class and extends
Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
*/
const Squaresuper = require('./5-square');

class Square extends Squaresuper {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
