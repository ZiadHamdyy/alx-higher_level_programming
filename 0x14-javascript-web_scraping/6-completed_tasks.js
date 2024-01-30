#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};
  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });
  console.log(completedTasks);
});
