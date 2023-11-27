#!/usr/bin/node

// Get the list of arguments excluding the script name
const args = process.argv.slice(2);

// Check if no argument or only one argument is passed
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers and sort in descending order
  const sortedIntegers = args.map(Number).sort((a, b) => b - a);

  // Print the second biggest integer
  console.log(sortedIntegers[1]);
}
