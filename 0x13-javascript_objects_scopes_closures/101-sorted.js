#!/usr/bin/node
const occurrencesDict = {};
const dict = require('./101-data').dict;
for (const userId in dict) {
  const occurrences = dict[userId];
  if (occurrences in occurrencesDict) {
    occurrencesDict[occurrences].push(userId);
  } else {
    occurrencesDict[occurrences] = [userId];
  }
}
console.log(occurrencesDict);
