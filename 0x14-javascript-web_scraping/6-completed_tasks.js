#!/usr/bin/node

// Import the built-in Node.js 'fs' module
const fs = require('fs');

// Import the 'request' module
const request = require('request');

// Use the 'request' module to perform an HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));


0x14-javascript-web_scraping/6-completed_tasks.js

#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const todos = JSON.parse(body);

      const completed = {};

      todos.forEach((todo) => {
        if (todo.completed) {
          if (completed[todo.userId] === undefined) {
            completed[todo.userId] = 1;
          } else {
            completed[todo.userId]++;
          }
        }
      });

      const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

      console.log(Object.keys(completed).length > 2 ? output : completed);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', error);
  }
});
