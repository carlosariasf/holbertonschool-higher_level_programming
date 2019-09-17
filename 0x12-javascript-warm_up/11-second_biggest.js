#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv[2] === 1) {
  console.log(0);
} else {
  let tmp = 0; let tmp2 = 0;
  for (let i = 0; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > tmp) {
      tmp = parseInt(process.argv[i]);
    }
  }
  for (let j = 0; j < process.argv.length; j++) {
    if (parseInt(process.argv[j]) > tmp2 && parseInt(process.argv[j]) !== tmp) {
      tmp2 = parseInt(process.argv[j]);
    }
  }
  console.log(tmp2);
}
