#!/usr/bin/node

if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of occurrences');
} else {
  let iterNum = parseInt(process.argv[2], 10);
  if (iterNum > 0) {
    for (i = 0; i < iterNum; i++) {
      console.log('C is fun');
    }
  }
}
