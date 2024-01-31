#!/usr/bin/node
// Prints users and all completed tasks
const request = require('request');
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    let results = body;
    if (typeof body === 'string') {
      results = JSON.parse(body);
    }
    const currentUsers = [];
    const listUsersTasks = [];
    const userCompleted = {};
    for (let index = 0; index < results.length; index++) {
      const id = results[index].userId;
      if (!currentUsers.includes(id)) {
        currentUsers.push(id);
        const myUser = { userId: id, completed: 0 };
        listUsersTasks.push(myUser);
      }
      if (results[index].completed) {
        for (let i = 0; i < listUsersTasks.length; i++) {
          if (listUsersTasks[i].userId === id) {
            listUsersTasks[i].completed++;
          }
        }
      }
    }
    for (let i = 0; i < listUsersTasks.length; i++) {
      if (listUsersTasks[i].completed !== 0) {
        userCompleted[listUsersTasks[i].userId] = listUsersTasks[i].completed;
      }
    }
    console.log(userCompleted);
  }
});
