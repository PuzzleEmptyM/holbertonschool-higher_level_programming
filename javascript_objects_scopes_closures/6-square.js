#!/usr/bin/node

// Import the Square class from 5. Square #0
const OldSquare = require('./5-square');

// Define the Square class that extends the OldSquare class
class Square extends OldSquare {
  // No need for the constructor if it doesn't add any functionality

  charPrint (c) {
    // If c is undefined, use the character 'X'; otherwise, use the specified character
    const printChar = c || 'X';

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(printChar.repeat(this.width));
    }
  }
}

// Export the Square class
module.exports = Square;
