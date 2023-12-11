#!/usr/bin/node

let i = 2;
let first = Number.MIN_SAFE_INTEGER;
let second = Number.MIN_SAFE_INTEGER;

if (process.argv.length <= 2) { console.log(0); } else {
  while (i < process.argv.length) {
    const current = parseInt(process.argv[i]);
    if (!isNaN(current)) {
      if (current > first) {
        second = first;
        first = current;
      } else if (current > second && current < first) { second = current; }
    }
    i++;
  }
  console.log(second === Number.MIN_SAFE_INTEGER ? 0 : second);
}
