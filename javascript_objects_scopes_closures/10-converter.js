#!/usr/bin/node

// Define the converter function
exports.converter = function (base) {
  // Return a function that takes a decimal number and converts it to the specified base
  return function (decimalNumber) {
    // Use the toString method with the specified base to convert the number
    return decimalNumber.toString(base);
  };
};
