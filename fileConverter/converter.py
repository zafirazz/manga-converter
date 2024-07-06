import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_images_to_pdf(input_folder):
    for root, dirs, files in os.walk(input_folder):
        for directory in dirs:
            folder_path = os.path.join(root, directory)
            image_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.jpg')])

            if image_files:
                output_pdf_path = os.path.join(input_folder, 'ilovemanga.pdf')
                c = canvas.Canvas(output_pdf_path, pagesize=letter)
                for image_file in image_files:
                    image_path = os.path.join(input_folder, image_file)
                    img = Image.open(image_path)
                    c.setPageSize((img.width, img.height))
                    c.drawImage(image_path, 0, 0)
                    c.showPage()
                c.save()
                print(f"PDF create successfully at {output_pdf_path}")

    image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')])
    if image_files:
        output_pdf_path = os.path.join(input_folder, 'output.pdf')
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            img = Image.open(image_path)
            c.setPageSize((img.width, img.height))
            c.drawImage(image_path, 0, 0)
            c.showPage()
        c.save()
        print(f"PDF created successfully at: {output_pdf_path}")