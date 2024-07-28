from flask import Flask, render_template, redirect, url_for, flash, jsonify, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import zipfile
from wtforms.validators import InputRequired, ValidationError
from flask_cors import CORS

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
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            app.logger.error("No file part in the request")
            return jsonify({"message": "No file part in the request"}), 400

        file = request.files['file']

        if file.filename == '':
            app.logger.error("No file selected for uploading")
            return jsonify({"message": "No file selected for uploading"}), 400

        if file and file.filename.endswith('.zip'):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

            unzip_file(save_path, app.config['UPLOAD_FOLDER'])

            app.logger.info(f"File {filename} uploaded successfully")
            return jsonify({"message": "File uploaded successfully"}), 200

        app.logger.error("Invalid file type")
        return jsonify({"message": "Invalid file type"}), 400

    except Exception as e:
        app.logger.error(f"Error during file upload: {e}")
        return jsonify({"message": "An error occurred during file upload"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)