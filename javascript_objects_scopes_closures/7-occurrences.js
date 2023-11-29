#!/usr/bin/node

// Define the nbOccurences function
exports.nbOccurences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  const occurrences = list.reduce((count, currentElement) => {
    // Increment count if the current element matches the search element
    return currentElement === searchElement ? count + 1 : count;
  }, 0);

  // Return the total number of occurrences
  return occurrences;
};
