import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (error, data) => {
      if (error) {
        reject(error);
        return;
      }

      const lines = data.trim().split('\n').slice(1);
      const students = {};

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!students[field]) {
          students[field] = [];
        }

        students[field].push(firstname);
      });

      resolve(students);
    });
  });
}

export default readDatabase;
