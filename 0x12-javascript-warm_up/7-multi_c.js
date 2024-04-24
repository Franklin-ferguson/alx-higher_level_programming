#!/usr/bin/node

// prints 3 lines: (like 1-multi_languages.js) but by
// using an array of string and a loop

const hey = 'C is fun';
for (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {	
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(hey);
  }
}
