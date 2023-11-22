#!/usr/bin/node

// Get number of arguments
const numArgs = process.argv.length - 2;

// Use console.log(...) to print the output based on args
if (numArgs === 0) {
    console.log('No argument');
} else if (numArgs === 1) {
    console.log('Argument found');
} else (numArgs === 2) {
    console.log('Arguments found');
}
