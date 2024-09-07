import re
from collections import Counter
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText


def center_window(window, width, height):
    # Center the window on the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def text_extract(pdf_file: str) -> list[str]:
    # Extracts text from the selected PDF file
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict=False)
        return [page.extract_text() for page in reader.pages]


def select_pdf_file():
    # Open a file dialog to select a PDF file and display its contents
    pdf_file = filedialog.askopenfilename(
        title="Select a PDF file", 
        filetypes=[("PDF files", "*.pdf")]
    )

    if pdf_file:
        try:
            extracted_text = text_extract(pdf_file)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, "\n".join(extracted_text))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read PDF: {e}")
    else:
        messagebox.showinfo("Cancelled", "File selection cancelled")


def copy_to_clipboard():
    #Append the contents of the text box to the clipboard
    current_clipboard = root.clipboard_get() if root.clipboard_get() else ""
    new_text = text_box.get(1.0, tk.END)
    combined_text = current_clipboard + new_text
    root.clipboard_clear()
    root.clipboard_append(combined_text)
    messagebox.showinfo("Copied", "Text copied to clipboard!")


# Create the main Tkinter window
root = tk.Tk()
root.title("PDF Reader")

# Set window size and center it on the screen
window_width = 600
window_height = 500
center_window(root, window_width, window_height)

# Add widgets
select_button = tk.Button(root, text="Select PDF", command=select_pdf_file)
select_button.pack(pady=10)
text_box = ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_box.pack(pady=10)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()