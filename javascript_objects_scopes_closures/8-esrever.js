#!/usr/bin/node

// Define the esrever function
exports.esrever = function (list) {
  // Check if the input is an array
  if (!Array.isArray(list)) {
    throw new Error('Input is not an array');
  }

  // Create a new array to store the reversed elements
  const reversedList = [];

  // Iterate through the original array in reverse order
  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversed array
    reversedList.push(list[i]);
  }

  // Return the reversed array
  return reversedList;
};
