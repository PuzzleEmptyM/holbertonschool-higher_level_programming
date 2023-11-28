#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// Define the Square class that extends Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the parent class (Rectangle)
    super(size, size);
  }
}

// Export the Square class
module.exports = Square;
