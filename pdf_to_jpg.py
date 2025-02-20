import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from pdf2image import convert_from_path


# Function to convert PDF to JPEG
def convert_pdf_to_jpeg(pdf_path, saving_folder):
    try:
        # Hardcoded Poppler path
        poppler_path = r'C:\poppler-24.08.0\Library\bin'  # add this folder to PATH

        # Convert the PDF pages to images
        pages = convert_from_path (pdf_path=pdf_path, poppler_path=poppler_path)

        # Saving each page as JPEG
        i = 1
        for page in pages:
            img_name = f'img-{i}.jpeg'
            page.save (os.path.join (saving_folder, img_name), "JPEG")
            i += 1

        messagebox.showinfo ("Success", "PDF has been converted to JPEG images!")
    except Exception as e:
        messagebox.showerror ("Error", f"An error occurred: {e}")


# Function to choose a folder to save the images
def choose_save_folder():
    folder = filedialog.askdirectory ()
    if folder:
        save_folder_entry.delete (0, tk.END)
        save_folder_entry.insert (0, folder)


# Function to choose a PDF file
def choose_pdf_file():
    pdf_file = filedialog.askopenfilename (filetypes=[("PDF files", "*.pdf")])
    if pdf_file:
        pdf_entry.delete (0, tk.END)
        pdf_entry.insert (0, pdf_file)


# Function to start the conversion
def start_conversion():
    pdf_path = pdf_entry.get ()
    save_folder = save_folder_entry.get ()

    if not pdf_path or not save_folder:
        messagebox.showwarning ("Input Error", "Please fill in all fields!")
    else:
        convert_pdf_to_jpeg (pdf_path, save_folder)


# Create the main window
root = tk.Tk ()
root.title ("PDF to JPEG Converter")

# Add UI elements
tk.Label (root, text="PDF File:").grid (row=0, column=0, padx=10, pady=5, sticky="e")
pdf_entry = tk.Entry (root, width=50)
pdf_entry.grid (row=0, column=1, padx=10, pady=5)
pdf_button = tk.Button (root, text="Browse", command=choose_pdf_file)
pdf_button.grid (row=0, column=2, padx=10, pady=5)

tk.Label (root, text="Save Folder:").grid (row=1, column=0, padx=10, pady=5, sticky="e")
save_folder_entry = tk.Entry (root, width=50)
save_folder_entry.grid (row=1, column=1, padx=10, pady=5)
save_folder_button = tk.Button (root, text="Browse", command=choose_save_folder)
save_folder_button.grid (row=1, column=2, padx=10, pady=5)

convert_button = tk.Button (root, text="Convert PDF to JPEG", command=start_conversion)
convert_button.grid (row=2, column=0, columnspan=3, padx=10, pady=20)

# Run the application
root.mainloop ()
