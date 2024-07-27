export const config = {
  api: {
    bodyParser: false,
  },
};

const multer = require('multer');
const upload = multer({ dest: '/tmp' });

const handler = (req, res) => {
  upload.single('file')(req, res, (err) => {
    if (err) {
      return res.status(500).json({ message: 'Upload failed' });
    }
    // Here you would handle the file upload to your Flask backend
    res.status(200).json({ message: 'File uploaded successfully' });
  });
};

export default handler;
