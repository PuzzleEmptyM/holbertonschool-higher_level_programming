#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // Create an empty object if conditions are not met
      return {};
    }

    // Initialize instance attributes
    this.width = w;
    this.height = h;
  }

  print () {
    // Check if width and height are valid before printing
    if (this.width > 0 && this.height > 0) {
      // Print the rectangle using the character X
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
