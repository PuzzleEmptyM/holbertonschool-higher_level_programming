#!/usr/bin/node

// Counter to keep track of the number of arguments printed
let argumentCount = 0;

// Define the logMe function
exports.logMe = function (item) {
  // Print the current count and argument value
  console.log(`${argumentCount}: ${item}`);

  // Increment the argument count for the next call
  argumentCount++;
};
