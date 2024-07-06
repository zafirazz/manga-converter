from flask import Flask, render_template, request, send_file
import os
import zipfile
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

