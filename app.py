import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog

class MyGui:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("QRcode")
        self.root.geometry("500x270")
        
        self.label = tk.Label(self.root, text="QR Code Generator", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        
        self.label1 = tk.Label(self.root, text="Enter text to convert into a QR code:", font=("Arial", 12))
        self.label1.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=1, font=("Arial", 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Generate QR Code", font=("Arial", 16), command=self.convert_to_qrcode)
        self.button.pack(padx=10, pady=30)

        self.root.mainloop()

    def convert_to_qrcode(self):
        
        # Gets the text from the input box
        text = self.textbox.get("1.0", tk.END).strip()

        # If no text entered, shows and error message
        if not text:
            messagebox.showinfo(title="Error", message="Enter text to convert!")
            return
        
        # Generates the QRcode
        img = qrcode.make(text)

        # Opening the file dialog to save the image at a certain location
        file_path = filedialog.asksaveasfilename( 
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save QR Code"
        )

        # Saves the image if a correct file path is provided
        if file_path:
            img.save(file_path)
        else:
            messagebox.showinfo(title="Error", message="Image not saved")
        

MyGui()