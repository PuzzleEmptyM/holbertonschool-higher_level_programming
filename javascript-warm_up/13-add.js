#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Export the add function as a property of the module object
module.exports.add = add;
