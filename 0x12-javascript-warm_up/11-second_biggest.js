#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = process.argv.slice(2);
  array.sort((a, b) => b - a);
  console.log(array[1]);
}
