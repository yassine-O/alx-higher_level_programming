#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = {};
  const todos = JSON.parse(body);
  for (const todo of todos) {
    if (todo.completed) {
      if (tasks[todo.userId] === undefined) {
        tasks[todo.userId] = 1;
      } else {
        tasks[todo.userId]++;
      }
    }
  }
  console.log(tasks);
});
