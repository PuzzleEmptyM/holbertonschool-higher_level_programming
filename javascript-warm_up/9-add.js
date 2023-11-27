#!/usr/bin/node

// Define the add function
function add (a, b) {
  return a + b;
}

// Get the two integers from the command-line arguments
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if both arguments are valid integers
if (isNaN(num1) || isNaN(num2)) {
  console.log('Invalid input. Please provide two integers');
} else {
  // Call the add function and print the result
  console.log(add(num1, num2));
}
