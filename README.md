# Project overview

The Manga to eBook Converter is a web-based application designed to streamline the process of converting manga images (JPG/PNG) into eBook formats (PDF) compatible with eReaders such as Kindle, PocketBook, Kobo and etc. This project addresses the common inconvenience of reading manga on mobile devices and the limitations of free online converters.

![manga1](https://github.com/user-attachments/assets/214de525-32d7-4acf-adf8-b7a57c0b68d0)


The backend of the project is built using Python and Flask, responsible for handling file uploads, processing images, and generating PDF files. And frontend was built with Next.js, HTML/CSS, JavaScript.

## Key Feautres
    - File Upload Endpoint: Accepts ZIP files containing manga chapters.
    - Extraction Module: Unzips the uploaded files and organizes images.
    - Image Processing Module: Converts images to a suitable format and arranges them into a PDF.
    - PDF Generation: Combines images into a single PDF file and prepares it for download.

# In order to run this project:

### Clone the Repository

```bash
git clone https://github.com/yourusername/manga-converter.git
cd manga-converter
```

### Run Flask Application
```bash
  python App.py
```

### Navigate to frontend
```bash
cd ../manga-frontend
```

###Install npm packages and start the development server
```bash
npm install
npm run dev
```

Open your web browser and navigate to http://localhost:3000 to use the Manga to eBook Converter. Enjoy! 

![manga2](https://github.com/user-attachments/assets/5a4989ec-7764-4df3-96e6-d3cacee14ba1)


