#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let n = x; n > 0; n--) {
    theFunction();
  }
};
