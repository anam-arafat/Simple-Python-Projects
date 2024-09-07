from typing import Final
import requests
import tkinter as tk
from tkinter import messagebox

# API key and base URL for the Cutt.ly API
API_KEY: Final[str] = 'YOUR_API_KEY'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_link(full_link: str) -> str:
    # Shortens the given URL using the Cutt.ly API
    payload = {'key': API_KEY, 'short': full_link}
    try:
        request = requests.get(BASE_URL, params=payload)
        request.raise_for_status()
        data = request.json()

        if url_data := data.get('url'):
            if url_data['status'] == 7:
                return url_data['shortLink']
            else:
                return f"Error status: {url_data['status']}"
        return "No URL data found in response"
    
    except requests.RequestException as e:
        return f"HTTP error occurred: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def on_shorten_button_click():
    # Handles the button click, shortens the URL, and shows the result or error
    url = url_entry.get()
    result = shorten_link(url)
    
    if result.startswith("http"):
        result_window = tk.Toplevel(window)
        result_window.title("Shortened URL")
        result_window.geometry('400x150+%d+%d' % (result_window.winfo_screenwidth() // 2 - 200, result_window.winfo_screenheight() // 2 - 75))
        
        tk.Label(result_window, text="Shortened URL:", font=('Helvetica', 12, 'bold')).pack(pady=10)
        result_var = tk.StringVar(value=result)
        result_entry = tk.Entry(result_window, textvariable=result_var, width=50, font=('Helvetica', 10), state='readonly')
        result_entry.pack(pady=10)
        
        def copy_to_clipboard():
            result_window.clipboard_append(result)
            messagebox.showinfo("Copied", "Shortened URL copied to clipboard!")
        
        tk.Button(result_window, text="Copy to Clipboard", command=copy_to_clipboard, font=('Helvetica', 10, 'bold')).pack(pady=10)
    else:
        messagebox.showerror("Error", result)

# Create the main window
window = tk.Tk()
window.title("URL Shortener")
window.geometry('400x200+%d+%d' % (window.winfo_screenwidth() // 2 - 200, window.winfo_screenheight() // 2 - 100))

# Widgets for input and shortening button
tk.Label(window, text="Enter URL:", font=('Helvetica', 12, 'bold')).pack(pady=10)
url_entry = tk.Entry(window, width=50, font=('Helvetica', 10))
url_entry.pack(pady=10)

shorten_button = tk.Button(window, text="Shorten URL", command=on_shorten_button_click, font=('Helvetica', 12, 'bold'))
shorten_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()