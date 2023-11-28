#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || typeof w !== 'number') {
      w = 0;
    }
    if (h <= 0 || typeof h !== 'number') {
      h = 0;
    }

    // Initialize instance attributes
    this.width = w;
    this.height = h;
  }
}

// Export the Rectangle class
module.exports = Rectangle;
