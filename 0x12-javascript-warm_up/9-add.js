#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

if (isNaN(add(process.argv[2], process.argv[3]))) { console.log('NaN'); } else { console.log(add(process.argv[2], process.argv[3])); }
