                                            #   QR code generator 
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
import io
import os

# Counter to keep track of QR image number
qr_counter = 1

def draw_gradient(canvas, width, height, r1, g1, b1, r2, g2, b2):
    steps = 100
    for i in range(steps):
        r = int(r1 + (r2 - r1) * i / steps)
        g = int(g1 + (g2 - g1) * i / steps)
        b = int(b1 + (b2 - b1) * i / steps)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_rectangle(0, i * (height/steps), width, (i+1)*(height/steps), outline="", fill=color)

def get_next_filename():
    i = 1
    while True:
        filename = f"qr_code_{i}.png"
        if not os.path.exists(filename):
            return filename
        i += 1

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter some data!")
        return

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Display in GUI
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    bio.seek(0)
    qr_image = Image.open(bio)
    qr_image = qr_image.resize((200, 200))
    photo = ImageTk.PhotoImage(qr_image)
    
    label_qr.config(image=photo)
    label_qr.image = photo

    # Save with a unique filename
    filename = get_next_filename()
    img.save(filename)
    messagebox.showinfo("Success", f"QR code saved as {filename}!")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

canvas = tk.Canvas(root, width=400, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Draw gradient from light blue to purple
draw_gradient(canvas, 400, 400, 0, 198, 225, 255, 110, 195)

# Create widgets
label = tk.Label(root, text="Enter text or URL:", font=('Arial', 12), bg="light blue")
entry = tk.Entry(root, width=30, font=('Arial', 12))
button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=('Arial', 12),bg="light pink",fg="black")
label_qr = tk.Label(root, bg="light pink")

# Place widgets on canvas
canvas.create_window(200, 40, window=label)
canvas.create_window(200, 80, window=entry)
canvas.create_window(200, 120, window=button)
canvas.create_window(200, 250, window=label_qr)

root.mainloop()
