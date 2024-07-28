const express = require('express');
const formidable = require('formidable');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 5000;
const UPLOAD_DIR = path.join(__dirname, 'uploads');

if (!fs.existsSync(UPLOAD_DIR)) {
  fs.mkdirSync(UPLOAD_DIR);
}

app.post('/upload', (req, res) => {
  const form = formidable({ multiples: true });

  form.uploadDir = UPLOAD_DIR;
  form.keepExtensions = true;

  form.parse(req, (err, fields, files) => {
    if (err) {
      res.status(500).json({ message: 'Error parsing the file' });
      return;
    }

    const file = files.file;
    if (!file) {
      res.status(400).json({ message: 'No file uploaded' });
      return;
    }

    const oldPath = file.filepath;
    const newPath = path.join(UPLOAD_DIR, file.originalFilename);

    fs.rename(oldPath, newPath, (err) => {
      if (err) {
        res.status(500).json({ message: 'Error saving the file' });
        return;
      }
      res.status(200).json({ message: 'File uploaded successfully' });
    });
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});