#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reverseList.push(list[index]);
  }
  return reverseList;
};
