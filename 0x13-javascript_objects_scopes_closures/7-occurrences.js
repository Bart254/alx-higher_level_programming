#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let total = 0;
  for (let index = 0; list[index]; index++) {
    if (list[index] === searchElement) {
      total++;
    }
  }
  return total;
};
