#!/usr/bin/node

// Get the first argument
const occuranceNumber = parseInt(process.argv[2]);

// Check if the argument can be converted to an integer
if (isNaN(occuranceNumber)) {
    console.log('Missing number of occurences');
} else {
    // Use a loop to print "C is fun" x times
    for (let i = 0; i < occuranceNumber; i++) {
        console.log('C is fun');
    }
}
