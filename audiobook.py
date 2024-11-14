from gtts import gTTS
import os
import threading
from tkinter import Tk, Label, Button, filedialog, messagebox

def create_audiobook(text_file, output_file):
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
        tts = gTTS(text=text, lang='en')
        tts.save(output_file)
        messagebox.showinfo("Success", f"Audiobook saved as {output_file}")
    except FileNotFoundError:
        messagebox.showerror("Error", "The selected text file was not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_text_file():
    global text_file
    text_file = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text Files", "*.txt")])
    if text_file:
        label_file_selected.config(text=f"Selected file: {text_file}")

def select_output_file():
    global output_file
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", title="Save audiobook as", filetypes=[("MP3 Files", "*.mp3")])
    if output_file:
        label_output_selected.config(text=f"Save as: {output_file}")

def play_audiobook():
    if output_file and os.path.exists(output_file):
        # Cross-platform play support
        if os.name == 'nt':  # Windows
            os.system(f"start {output_file}")
        elif os.name == 'posix':  # macOS or Linux
            if "darwin" in os.uname().sysname.lower():  # macOS
                os.system(f"open {output_file}")
            else:  # Linux
                os.system(f"xdg-open {output_file}")
    else:
        messagebox.showerror("Error", "Audiobook file not found. Please create an audiobook first.")

def create_audiobook_async():
    if text_file and output_file:
        # Run the audiobook creation in a separate thread
        threading.Thread(target=create_audiobook, args=(text_file, output_file)).start()
    else:
        messagebox.showwarning("Warning", "Please select a text file and a save location.")

# Initialize the main window
root = Tk()
root.title("Audiobook Creator")
root.geometry("400x250")

text_file = ""
output_file = "audiobook.mp3"

# GUI Elements
Label(root, text="RealJe-emy Audiobook Creator", font=("Arial", 16)).pack(pady=10)

Button(root, text="Select Text File", command=select_text_file).pack(pady=5)
label_file_selected = Label(root, text="No file selected", font=("Arial", 10))
label_file_selected.pack()

Button(root, text="Choose Save Location", command=select_output_file).pack(pady=5)
label_output_selected = Label(root, text="Default: audiobook.mp3", font=("Arial", 10))
label_output_selected.pack()

Button(root, text="Create Audiobook", command=create_audiobook_async).pack(pady=10)
Button(root, text="Play Audiobook", command=play_audiobook).pack(pady=5)

# Run the GUI
root.mainloop()
