import os

from pdf2image import convert_from_path

poppler_path = r'C:\Program Files (x86)\poppler-0.68.0\bin'
pdf_path = r'C:\Users\GIGACHAD\PycharmProjects\pdf_to_jpeg\pdf\ticket.pdf'

pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
saving_folder = r'C:\Users\GIGACHAD\PycharmProjects\pdf_to_jpeg\jpg'

i = 1

for page in pages:
    img_name = f'img-{i}.jpeg'
    page.save(os.path.join(saving_folder, img_name), "JPEG")
    i += 1
