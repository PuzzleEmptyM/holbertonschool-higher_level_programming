#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
  }
}

// Get the integer from the command-line argument
const num = parseInt(process.argv[2]);

// Call the factorial function and print the result
console.log(factorial(num));
