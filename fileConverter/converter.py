import os
import zipfile
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_images_to_pdf(input_folder):
    output_folder = os.path.join(input_folder, 'output_pdfs')
    os.makedirs(output_folder, exist_ok=True)

    try:
        for root, dirs, files in os.walk(input_folder):
            for directory in dirs:
                folder_path = os.path.join(root, directory)
                image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png'))])

                if image_files:
                    output_pdf_path = os.path.join(output_folder, f'{directory}.pdf')
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
            output_pdf_path = os.path.join(output_folder, 'root_images.pdf')
            c = canvas.Canvas(output_pdf_path, pagesize=letter)

            for image_file in root_image_files:
                image_path = os.path.join(input_folder, image_file)
                img = Image.open(image_path)
                c.setPageSize((img.width, img.height))
                c.drawImage(image_path, 0, 0, width=img.width, height=img.height)
                c.showPage()
            c.save()
            print(f"PDF created successfully at {output_pdf_path}")

        # Zip the output folder
        zip_output_path = os.path.join(input_folder, 'output_pdfs.zip')
        with zipfile.ZipFile(zip_output_path, 'w') as zipf:
            for root, _, files in os.walk(output_folder):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_folder))
        print(f"All PDFs zipped successfully at {zip_output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
convert_images_to_pdf('/home/marbelle/Downloads/jujutsu-kaisen_c141_c150')
