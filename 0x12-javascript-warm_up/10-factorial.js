#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
function factorial (a) {
  if (a >= 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
