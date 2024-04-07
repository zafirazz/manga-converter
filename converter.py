import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_images_to_pdf(input_folder):
    image_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.jpg')])

    output_pdf_path = os.path.join(input_folder, 'noragami ch50.pdf')
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        img = Image.open(image_path)
        c.setPageSize((img.width, img.height))
        c.drawImage(image_path, 0, 0)
        c.showPage()

    c.save()

    print(output_pdf_path)


input_folder = '/home/marbelle/Documents/manga/noragami_c041 _ c050/c050'
convert_images_to_pdf(input_folder)
