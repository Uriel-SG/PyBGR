import os
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import ttkbootstrap as tb

def remove_background(input_image_path, output_image_path):
    with Image.open(input_image_path) as img:
        result = remove(img)
        result.save(output_image_path)

def browse_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp")]
    )
    if file_path:
        app.selected_image = file_path
        image_label.config(text=os.path.basename(file_path), foreground="#90caf9")

def remove_bg_action():
    if not hasattr(app, 'selected_image') or not app.selected_image:
        messagebox.showwarning("No image", "Please select an image first.")
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save output image"
    )
    if save_path:
        try:
            remove_background(app.selected_image, save_path)
            messagebox.showinfo("Success", f"Background removed and saved:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# --- GUI ---
app = tb.Window(themename="darkly")
app.title("PyRBG - Remove BG")
app.geometry("400x370")
app.resizable(False, False)
app.configure(bg="#222831")

# Percorso della cartella dove si trova lo script
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Icona della finestra
icon_path = os.path.join(BASE_PATH, "pybgr.ico")
if os.path.exists(icon_path):
    app.iconbitmap(icon_path)

# Logo App
logo_path = os.path.join(BASE_PATH, "pybgr.png")

if os.path.exists(logo_path):
    logo_img = Image.open(logo_path).resize((230, 130))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tb.Label(app, image=logo_photo, background="#222831")
    logo_label.image = logo_photo
    logo_label.pack(pady=(22, 10))
else:
    logo_label = tb.Label(app, text="RemoveBG", font=("Segoe UI", 24, "bold"), background="#222831", foreground="#90caf9")
    logo_label.pack(pady=(32, 10))

# Selettore immagine
image_label = tb.Label(app, text="No image selected", font=("Segoe UI", 10), background="#222831", foreground="#b0b0b0")
image_label.pack(pady=(10, 5))

browse_btn = tb.Button(app, text="Sfoglia immagine...", bootstyle="info-outline", command=browse_image)
browse_btn.pack(pady=5)

remove_btn = tb.Button(app, text="Remove Background", bootstyle="success", width=20, command=remove_bg_action)
remove_btn.pack(pady=22)

app.mainloop()
