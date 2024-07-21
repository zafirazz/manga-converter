# # from flask import Flask, flash, redirect, url_for, render_template, request, send_file
# # import os
# # import zipfile
# # from PIL import Image
# # from reportlab.lib.pagesizes import letter
# # from reportlab.pdfgen import canvas
# # from werkzeug.utils import secure_filename
# # import fileConverter
#
# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import FileField, SubmitField
# from werkzeug.utils import secure_filename
# import os
# from wtforms.validators import InputRequired
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'supersecretkey'
# app.config['UPLOAD_FOLDER'] = 'statics/files'
#
# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Upload File")
#
# @app.route('/', methods=['GET',"POST"])
# @app.route('/home', methods=['GET',"POST"])
# def home():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data # First grab the file
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
#         return "File has been uploaded."
#     return render_template('index.html', form=form)
#
# if __name__ == '__main__':
#     app.run(debug=False)

# from flask import Flask, render_template, redirect, url_for, flash
# from flask_wtf import FlaskForm
# from wtforms import FileField, SubmitField
# from werkzeug.utils import secure_filename
# import os
# from wtforms.validators import InputRequired, ValidationError
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'supersecretkey'
# app.config['UPLOAD_FOLDER'] = 'static/files'
#
#
# def file_extension_check(form, field):
#     if not (field.data.filename.endswith('.png') or field.data.filename.endswith('.jpg') or
#             field.data.filename.endswith('.jpeg') or field.data.filename.endswith('.zip')):
#         raise ValidationError('File must be .png, .jpg, .jpeg, or .zip')
#
#
# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired(), file_extension_check])
#     submit = SubmitField("Upload File")
#
#
# @app.route('/', methods=['GET', "POST"])
# @app.route('/home', methods=['GET', "POST"])
# def home():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data  # First grab the file
#         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
#                                secure_filename(file.filename)))  # Then save the file
#         # return "File has been uploaded."
#         flash("File has been uploaded.", "success")
#         return redirect(url_for('upload_success'))
#     return render_template('index.html', form=form)
#
#
# @app.route('/upload_success')
# def upload_success():
#     return render_template('upload_success.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import zipfile
from wtforms.validators import InputRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


def file_extension_check(form, field):
    if not (field.data.filename.endswith('.png') or field.data.filename.endswith('.jpg') or
            field.data.filename.endswith('.jpeg') or field.data.filename.endswith('.zip')):
        raise ValidationError('File must be .png, .jpg, .jpeg, or .zip')


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
