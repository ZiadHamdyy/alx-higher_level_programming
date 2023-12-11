#!/usr/bin/node
let i = 0;
if (parseInt(process.argv[2]))
  while (i < parseInt(process.argv[2]))
  {
    console.log('C is fun');
    i++;
  }
else
  console.log('Missing number of occurrences');
