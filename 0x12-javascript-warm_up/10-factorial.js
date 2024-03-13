#!/usr/bin/node
function fact (N) {
  if (isNaN(N) || N === 0) {
    return 1;
  }
  return N * fact(N - 1);
}
console.log(fact(parseInt(process.argv[2])));
