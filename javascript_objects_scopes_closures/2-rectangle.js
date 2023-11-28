#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number'
    || typeof h !== 'number') {
      // Create an instance with default values if conditions are not met
      this.width = 0;
      this.height = 0;
    } else {
      // Initialize instance attributes
      this.width = w;
      this.height = h;
    }
  }
}

// Export the Rectangle class
module.exports = Rectangle;
