#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  for (let index = 2; index < args.length; index++) {
    args[index] = parseInt(args[index]);
  }
  args.sort(function (a, b) { return b - a; });
  console.log(args[3]);
}
