import os
import zipfile

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_images_to_pdf(input_folder):
    result_folder = os.path.join(input_folder, 'output_pdf_folder')
    os.makedirs(result_folder, exist_ok=True)

    count = 1

    try:
        for root, dirs, files in os.walk(input_folder):
            for directory in dirs:
                folder_path = os.path.join(root, directory)
                image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.jpg', '.png')])

                #TODO: resolve the sorting of chapters in new folder
                if image_files:
                    output_pdf_path = os.path.join(result_folder, f'{count}.pdf')
                    count+=1
                    c = canvas.Canvas(output_pdf_path, pagesize=letter)

                    for image_file in image_files:
                        image_path = os.path.join(folder_path, image_file)
                        img = Image.open(image_path)
                        c.setPageSize((img.width, img.height))
                        c.drawImage(image_path, 0, 0, width=img.width, height=img.height)
                        c.showPage()
                    c.save()
                    print(f"PDF created successfully at {output_pdf_path}")

        root_image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.png'))])
        if root_image_files:
            output_pdf_path = os.path.join(input_folder, f'{count}.pdf')
            c = canvas.Canvas(output_pdf_path, pagesize=letter)

            for image_file in root_image_files:
                image_path = os.path.join(input_folder, image_file)
                img = Image.open(image_path)
                c.setPageSize((img.width, img.height))
                c.drawImage(image_path, 0, 0, width=img.width, height=img.height)
                c.showPage()
            c.save()
            print(f"PDF created successfully at {output_pdf_path}")

            #TODO: zipping is not working, review it and rewrite or possibly create different class for that
            zip_output_folder = os.path.join(input_folder, 'output_zip_folder')
            with zipfile.ZipFile(output_pdf_path, 'w', zipfile.ZIP_DEFLATED) as zip:
                for root, dirs, files in os.walk(result_folder):
                    for file in files:
                        zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), result_folder))
                print(f"Zip created successfully at {zip_output_folder}")
    except FileNotFoundError as ex:
        print(ex)

convert_images_to_pdf('/home/marbelle/Downloads/jujutsu-kaisen_c141 _ c150')
