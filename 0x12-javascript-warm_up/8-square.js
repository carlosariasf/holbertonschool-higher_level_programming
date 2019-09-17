#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    let sq = '';
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      sq += '#';
    }
    console.log(sq)
  }
}
