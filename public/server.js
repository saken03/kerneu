const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/api/products', (req, res) => {
  fs.readFile('data.json', (err, data) => {
    if (err) {
      res.status(500).send('Error reading data');
    } else {
      res.json(JSON.parse(data));
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running at  http://localhost:${port}`);
});