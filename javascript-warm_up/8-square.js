#!/usr/bin/node

// Get the size of the square from the first argument
const sizeSquare = parseInt(process.argv[2]);

// Check if the argument can be converted to an integer
if (isNaN(sizeSquare)) {
  console.log('Missing size');
} else {
  // Use nested loops to print the square
  for (let i = 0; i < sizeSquare; i++) {
    let row = '';
    for (let j = 0; j < sizeSquare; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
