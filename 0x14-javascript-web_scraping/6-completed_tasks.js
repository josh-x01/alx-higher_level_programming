#!/usr/bin/node

require('request')(process.argv[2], (e, r, b) => {
  if (e) console.log(e);
  else {
    const CompletedTasks = {};
    for (let i = 1; i <= 10; i++) {
      CompletedTasks[i] = JSON.parse(b).filter(task => task.completed === true)
        .filter(task => task.userId === i).length;
    }
    console.log(CompletedTasks);
  }
});
