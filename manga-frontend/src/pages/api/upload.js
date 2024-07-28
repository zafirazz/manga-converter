// src/pages/api/upload.js
import formidable from 'formidable';
import fs from 'fs';
import path from 'path';

export const config = {
  api: {
    bodyParser: false,
  },
};

const upload = async (req, res) => {
  const form = new formidable.IncomingForm();

  form.uploadDir = './public/uploads';
  form.keepExtensions = true;

  form.parse(req, (err, fields, files) => {
    if (err) {
      return res.status(500).json({ message: 'Error parsing the files' });
    }

    const file = files.file;
    const oldPath = file.filepath;
    const newPath = path.join(form.uploadDir, file.originalFilename);

    fs.rename(oldPath, newPath, (err) => {
      if (err) throw err;
      res.status(200).json({ message: 'File uploaded successfully' });
    });
  });
};

export default upload;
