#!/usr/bin/node

// Get number of arguments
const firstArg = process.argv[2];

// Use console.log(...) to print the output based on args
if (typeof firstArg === 'undefined') {
  console.log('No argument');
} else {
  console.log(firstArg);
}
