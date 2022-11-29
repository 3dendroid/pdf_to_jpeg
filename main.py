from pdf2image import convert_from_path

pages = convert_from_path('', 500)

# Saving pages in jpeg format

for page in pages:
    page.save('NDA.jpg', 'JPEG')
