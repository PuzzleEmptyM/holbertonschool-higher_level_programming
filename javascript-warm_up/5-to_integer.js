#!/usr/bin/node

// Get number of arguments
const firstArg = process.argv[2];

// Convert arg to integer
const argInt = parseInt(firstArg);

// Use console.log(...) to print the output based on args
if (!isNaN(argInt)) {
  console.log(`My number: ${argInt}`);
} else {
  console.log('Not a number');
}
