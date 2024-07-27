from flask import Flask, render_template, redirect, url_for, flash
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


@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        save_path = save_file(file)

        if filename.endswith('.zip'):
            extract_to = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'])
            unzip_file(save_path, extract_to)
            os.remove(save_path)  # Optionally remove the ZIP file after extraction

        flash("File has been uploaded.", "success")
        return redirect(url_for('upload_success'))

    for error in form.errors.values():
        flash(error[0], "danger")

    return render_template('index.html', form=form)


@app.route('/upload_success')
def upload_success():
    return render_template('upload_success.html')


if __name__ == '__main__':
    app.run(debug=True)
