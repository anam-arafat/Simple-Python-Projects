import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import io

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, user_input: str, fg: str, bg: str):
        #Generate a QR code image from the user input
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            return qr_image
        except Exception as e:
            raise Exception(f'Error: {e}')

def center_window(window, width, height):
    #Center the window on the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def show_qr_image():
    #Display the generated QR code in a new window
    user_input = text_entry.get()
    if not user_input:
        messagebox.showerror("Input Error", "Text entry cannot be empty!")
        return
    
    try:
        myqr = MyQR(size=10, padding=2)  # QR code parameters
        qr_image = myqr.create_qr(user_input, fg='black', bg='white')

        # Convert image to PhotoImage for Tkinter
        with io.BytesIO() as byte_stream:
            qr_image.save(byte_stream, format='PNG')
            qr_photo = ImageTk.PhotoImage(Image.open(io.BytesIO(byte_stream.getvalue())))
        
        result_window = tk.Toplevel(root)
        result_window.title("QR Code")

        # Adjust window size to fit QR code and center it
        qr_width, qr_height = qr_image.size
        window_width = qr_width + 50
        window_height = qr_height + 100
        center_window(result_window, window_width, window_height)
        
        # Display the QR code image
        qr_label = tk.Label(result_window, image=qr_photo)
        qr_label.image = qr_photo
        qr_label.pack(pady=10)

        # Download button functionality
        def download_qr():
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            if save_path:
                try:
                    qr_image.save(save_path)
                    messagebox.showinfo("Success", "QR Code saved successfully!")
                except Exception as e:
                    messagebox.showerror("Save Error", f"Failed to save QR code: {e}")
        
        download_button = tk.Button(result_window, text="Download QR Code", command=download_qr)
        download_button.pack(pady=10)

    except Exception as e:
        messagebox.showerror("QR Generation Error", str(e))

# Create the main Tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# Set main window size and center it
window_width = 400
window_height = 200
center_window(root, window_width, window_height)

# Input text entry
tk.Label(root, text="Enter text for QR code:", font=('Helvetica', 12, 'bold')).pack(pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

# Generate QR button
generate_button = tk.Button(root, text="Generate QR Code", command=show_qr_image)
generate_button.pack(pady=20)

root.mainloop()