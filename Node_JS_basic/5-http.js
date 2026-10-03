const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');

    const logs = [];
    const originalLog = console.log;

    console.log = (message) => {
      logs.push(message);
    };

    countStudents(database)
      .then(() => {
        console.log = originalLog;
        res.end(logs.join('\n'));
      })
      .catch((error) => {
        console.log = originalLog;
        res.end(error.message);
      });
  }
});

app.listen(1245);

module.exports = app;
