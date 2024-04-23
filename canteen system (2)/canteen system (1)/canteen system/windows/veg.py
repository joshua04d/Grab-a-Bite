import customtkinter as ct
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

# Create a CTk() instance
s = ct.CTk()

# Frame settings
width = 1310
height = 550
s.geometry(f"{width}x{height}+90+265")
s.overrideredirect(1)

# Main window frame
main_f = ct.CTkFrame(master=s, height=height - 150, width=width - 50, fg_color="black")
main_f.pack(side=ct.TOP, pady=20)
main_f.propagate(False)

# Placeholder for images
images_frame = ct.CTkFrame(master=main_f, height=300, width=width - 50, fg_color="black")
images_frame.pack(side=ct.TOP, pady=20)

# Buttons below images
buttons_frame = ct.CTkFrame(master=main_f, height=100, width=width - 50, fg_color="black")
buttons_frame.pack(side=ct.TOP, pady=20)

# Function to handle button clicks and record them in the database
def button_click(button_text, cost):
    # Record the button click in the database
    conn = sqlite3.connect('button_clicks.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS button_clicks (button_text TEXT, cost REAL)")
    c.execute("INSERT INTO button_clicks (button_text, cost) VALUES (?, ?)", (button_text, cost))
    # Update the cost of the food item if it's one of the specified items
    if button_text == "veg fried rice":
        c.execute("UPDATE button_clicks SET cost=? WHERE button_text=?", (40, button_text))
    elif button_text == "dosa":
        c.execute("UPDATE button_clicks SET cost=? WHERE button_text=?", (35, button_text))
    elif button_text == "spring roll":
        c.execute("UPDATE button_clicks SET cost=? WHERE button_text=?", (25, button_text))
    elif button_text == "veg noodles":
        c.execute("UPDATE button_clicks SET cost=? WHERE button_text=?", (45, button_text))
    conn.commit()
    conn.close()
    # Show message box
    messagebox.showinfo("", f"'{button_text}' added")

# Create placeholders for images (4 images in a row)
image_paths = ['windows/images/vfr.jpg', 'windows/images/d.jpg', 'windows/images/sr.jpg', 'windows/images/vn.jpg']
for i, image_path in enumerate(image_paths):
    image = Image.open(image_path)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    image_placeholder = ct.CTkLabel(
        images_frame,
        image=photo,
        width=200,
        height=200,
        bg_color="lightgrey"
    ) 
    image_placeholder.image = photo
    image_placeholder.grid(row=0, column=i, padx=30)

# Define button names
button_info = [("veg fried rice", 40), ("dosa", 35), ("spring roll", 25), ("veg noodles", 45)]

# Create buttons below images
for i, (button_text, cost) in enumerate(button_info):
    button = ct.CTkButton(
        buttons_frame,
        text=button_text,
        font=('Consolas', 18),
        width=50,
        height=35,
        corner_radius=10,
        bg_color="black",
        command=lambda bt=button_text, c=cost: button_click(bt, c)
    )
    button.grid(row=0, column=i, padx=90)
    
# BACK button
btn_back = ct.CTkButton(
    master=s,
    text="BACK",
    font=('Consolas', 12, 'bold'),
    command=lambda: clear(),
    width=100,
    height=40,
    corner_radius=10,
    fg_color="grey",
)
btn_back.place(x=1080, y=350)

def clear():
    s.destroy()

# Start the main event loop
s.mainloop()
