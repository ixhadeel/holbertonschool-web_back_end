const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const logs = [];
  const originalLog = console.log;

  console.log = (message) => {
    logs.push(message);
  };

  countStudents(database)
    .then(() => {
      console.log = originalLog;
      res.type('text/plain');
      res.send(`This is the list of our students\n${logs.join('\n')}`);
    })
    .catch((error) => {
      console.log = originalLog;
      res.type('text/plain');
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
