#!/usr/bin/node

require('request')(process.argv[2], (e, r, b) => {
  if (e) console.log(e);
  const CompletedTasks = {};
  for (let i = 1; i <= 10; i++) {
    const n = JSON.parse(b).filter(task => task.completed === true)
      .filter(task => task.userId === i).length;
    if (n) CompletedTasks[i] = n;
  }
  console.log(CompletedTasks);
});
