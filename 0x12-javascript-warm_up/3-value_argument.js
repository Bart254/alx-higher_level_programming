#!/usr/bin/node
'use strict';
const args = process.argv;
if (!args[2]) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
