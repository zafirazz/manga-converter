from flask import Flask, render_template, redirect, url_for, flash, jsonify, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import zipfile
from wtforms.validators import InputRequired, ValidationError
from flask_cors import CORS
import threading

from fileConverter.converter import convert_images_to_pdf

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': "http://localhost:3000"}})
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

def file_extension_check(form, field):
    if not (field.data.filename.endswith('.zip')):
        raise ValidationError('File must be .zip')

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired(), file_extension_check])
    submit = SubmitField("Upload File")

def save_file(file):
    filename = secure_filename(file.filename)
    save_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], filename)
    file.save(save_path)
    return save_path

def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            # Identify the root folder by inspecting the first file's directory structure
            root_folder = None
            for name in zip_ref.namelist():
                if '/' in name:
                    root_folder = name.split('/')[0]
                    break
            return root_folder
    except Exception as e:
        app.logger.error(f"Failed to unzip file: {e}")
        raise e

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({"message": "No file part in the request"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"message": "No file selected for uploading"}), 400

        if file and file.filename.endswith('.zip'):
            save_path = save_file(file)

            root_folder = unzip_file(save_path, app.config['UPLOAD_FOLDER'])

            if root_folder:
                input_folder = os.path.join(app.config['UPLOAD_FOLDER'], root_folder)
                # Start the conversion process in a separate thread
                conversion_thread = threading.Thread(target=convert_images_to_pdf, args=(input_folder,))
                conversion_thread.start()
                app.logger.info(f"File {file.filename} uploaded and unzipped successfully")
                return jsonify({"message": "File uploaded and unzipped successfully", "root_folder": root_folder}), 200
            else:
                return jsonify({"message": "Failed to unzip the file"}), 500

        return jsonify({"message": "Invalid file type"}), 400

    except Exception as e:
        app.logger.error(f"Error during file upload: {e}")
        return jsonify({"message": "An error occurred during file upload"}), 500

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    if filename != 'result_folder.zip':
        return jsonify({"message": "Invalid file name"}), 400

    uploads = os.path.join(app.config['UPLOAD_FOLDER'])
    result_zip_path = os.path.join(uploads, filename)

    if not os.path.exists(result_zip_path):
        return jsonify({"message": "The result file is not ready yet. Please try again later."}), 404

    return send_from_directory(directory=uploads, path=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)