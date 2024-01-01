#!/usr/bin/node
const fs = require('fs');
const [, , file1, file2, file3] = process.argv;
const data1 = fs.readFileSync(file1, 'utf-8');
const data2 = fs.readFileSync(file2, 'utf-8');
const data3 = data1 + data2;
fs.writeFileSync(file3, data3);
