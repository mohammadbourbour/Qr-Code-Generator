"""
Qr Code Generator

Made by : Mohammad boorboor
Email : m.boorboor315@gmail.com

"""

# Refrences

import qrcode
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import tempfile


class QRCodeGenerator:
    def __init__(self):
        # Create a GUI window
        self.root = tk.Tk()
        self.root.title("QR Code Generator")

        # Create input fields for the text, output file name, name, and email
        tk.Label(self.root, text="QR Code text:").grid(row=0, column=0, padx=10, pady=10)
        self.qr_text_entry = tk.Entry(self.root, width=50)
        self.qr_text_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="File Name:").grid(row=1, column=0, padx=10, pady=10)
        self.output_file_entry = tk.Entry(self.root, width=30)
        self.output_file_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Made by: Mohammad boorboor").grid(row=2, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Email: m.boorboor315@gmail.com").grid(row=3, column=0, padx=10, pady=10)

        tk.Label(self.root, text="Github: www.github.com/mohammadboorboor").grid(row=4, column=0, padx=10, pady=10)

        # Create a button to generate the QR code
        generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code)
        generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Create a label to display messages
        self.message_label = tk.Label(self.root, text="")
        self.message_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Create a canvas to display the QR code preview
        self.qr_canvas = tk.Canvas(self.root, width=250, height=250, bg="white")
        self.qr_canvas.grid(row=0, column=2, rowspan=6, padx=10, pady=10)

    def run(self):
        self.root.mainloop()

    def generate_qr_code(self):
        # Get the text and output file name from the input fields
        qr_text = self.qr_text_entry.get()
        output_file_name = self.output_file_entry.get()

        # Validate the output file name
        output_file_name = re.sub(r"[^\w\-_. ]", '', output_file_name)

        # Generate the QR code using qrcode library
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(qr_text)
        qr.make(fit=True)

        # Create an image from the QR code and save it to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(temp_file.name)

        # Load the image from the temporary file into a PhotoImage object and display it on the canvas
        self.qr_image = tk.PhotoImage(file=temp_file.name)
        self.qr_canvas.delete("all")
        self.qr_canvas.create_image(0, 0, anchor="nw", image=self.qr_image)

        # Update the message label with a success message
        self.message_label.config(text="QR code successfully generated")

        # Ask the user if they want to save the QR code image
        if messagebox.askyesno(title="Save QR Code", message="Do you want to save the QR code image?"):
            # Use a file dialog to let the user choose the file name and location
            output_file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=output_file_name)

            if output_file_path:
                # Copy the temporary file to the user-selected file path
                os.replace(temp_file.name, output_file_path)

                # Update the message label with a success message
                self.message_label.config(text=f"QR code successfully generated and saved as {output_file_path}")
        else:
            # Delete the temporary file
            os.remove(temp_file.name)

            # Update the message label with a cancellation message
            self.message_label.config(text="QR code generation cancelled by user")


# Create an instance of the QRCodeGenerator class and run the app
qr_generator = QRCodeGenerator()
qr_generator.run()
