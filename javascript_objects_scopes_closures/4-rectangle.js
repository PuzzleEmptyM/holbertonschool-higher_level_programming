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
      // Print the rectangle using the character 'X'
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    // Exchange the width and height of the rectangle
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Multiply the width and height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
};
