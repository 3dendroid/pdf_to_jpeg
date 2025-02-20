import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from PIL import Image


# Function to convert JPG to PDF
def convert_jpg_to_pdf(jpg_paths, saving_folder, output_filename):
    try:
        # Open the first image to start the PDF
        images = [Image.open(jpg) for jpg in jpg_paths]

        # Convert the list of images into a PDF
        pdf_path = os.path.join(saving_folder, output_filename + ".pdf")
        images[0].save(pdf_path, save_all=True, append_images=images[1:], resolution=100.0, quality=95, optimize=True)

        messagebox.showinfo("Success", f"JPG images have been converted to PDF! Saved as {pdf_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Function to choose JPG files
def choose_jpg_files():
    jpg_files = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg;*.jpeg")])
    if jpg_files:
        jpg_listbox.delete(0, tk.END)
        for jpg in jpg_files:
            jpg_listbox.insert(tk.END, jpg)


# Function to choose a folder to save the PDF
def choose_save_folder():
    folder = filedialog.askdirectory()
    if folder:
        save_folder_entry.delete(0, tk.END)
        save_folder_entry.insert(0, folder)


# Function to start the conversion
def start_conversion():
    # Get the list of selected JPG files and save folder
    jpg_paths = list(jpg_listbox.get(0, tk.END))
    save_folder = save_folder_entry.get()
    output_filename = output_filename_entry.get()

    if not jpg_paths or not save_folder or not output_filename:
        messagebox.showwarning("Input Error", "Please fill in all fields and select at least one JPG file!")
    else:
        convert_jpg_to_pdf(jpg_paths, save_folder, output_filename)


# Create the main window
root = tk.Tk()
root.title("JPG to PDF Converter")

# Add UI elements
tk.Label(root, text="Select JPG Files:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
jpg_button = tk.Button(root, text="Browse", command=choose_jpg_files)
jpg_button.grid(row=0, column=1, padx=10, pady=5)

jpg_listbox = tk.Listbox(root, width=60, height=10)
jpg_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

tk.Label(root, text="Save Folder:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
save_folder_entry = tk.Entry(root, width=50)
save_folder_entry.grid(row=2, column=1, padx=10, pady=5)
save_folder_button = tk.Button(root, text="Browse", command=choose_save_folder)
save_folder_button.grid(row=2, column=2, padx=10, pady=5)

tk.Label(root, text="Output Filename:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
output_filename_entry = tk.Entry(root, width=50)
output_filename_entry.grid(row=3, column=1, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert JPG to PDF", command=start_conversion)
convert_button.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

# Run the application
root.mainloop()
