import customtkinter as ct
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import tkinter as tk
import sqlite3
import subprocess

s = ct.CTk()
#<-----------frame settings-------------->
width=1000
height=600
# x=(s.winfo_screenwidth()//15)-(-width//10)
# y=(s.winfo_screenheight()//2)-(height//2)
s.geometry("1350x740+60+50")


#<-------------xxxxx------------------->

#<-----------Navbar------------>
nav = ct.CTkFrame(master=s, height=100, width=1300, fg_color="black")
nav.pack(side=ct.TOP, padx=7, pady=10)
#<-----------xxxx------------->

#<----------Main window--------------->
main_f = ct.CTkFrame(master=s, height=600, width=1300, fg_color="black")
main_f.pack(side=ct.TOP, pady=50)  # Align the main window below the navbar
main_f.propagate(False)

#<------------logo-------------->
lbl = ct.CTkLabel(
    nav,
    text="GRAB A ",
    font=('Game of Squids',20,'bold')
).place(x=12,y=15)

lb2 = ct.CTkLabel(
    nav,
    text="BITE",
    font=('Game of Squids',20,'bold')
).place(x=25,y=45)

#<-------------buttons--------------->
#menu BUTTON
add_S = ct.CTkButton(
    master=nav,
    text='Snacks',
    font=('Consolas',15,'bold'),
    fg_color="grey",
    width=100,
    height=40,
    corner_radius=10,
    hover_color="pink",
    text_color="orange",
    command=lambda:snacks()
).place(x=150,y=35)


#veg items
add_S = ct.CTkButton(
    master=nav,
    text='Veg',
    font=('Consolas',15,'bold'),
    fg_color="grey",
    width=100,
    height=40,
    corner_radius=10,
    hover_color="pink",
    text_color="orange",
    command=lambda:veg()
).place(x=300,y=35)

#non-veg items
add_S = ct.CTkButton(
    master=nav,
    text='non-Veg',
    font=('Consolas',15,'bold'),
    fg_color="grey",
    width=100,
    height=40,
    corner_radius=10,
    hover_color="pink",
    text_color="orange",
    command=lambda:nonveg()
).place(x=450,y=35)

#drinks
add_S = ct.CTkButton(
    master=nav,
    text='Drink',
    font=('Consolas',15,'bold'),
    fg_color="grey",
    width=100,
    height=40,
    corner_radius=10,
    hover_color="pink",
    text_color="orange",
    command=lambda:drinks()
).place(x=600,y=35)


#cart
def cart():
    os.system('python windows\\cart.py')

add_S = ct.CTkButton(
    master=nav,
    text='cart',
    font=('Consolas', 15, 'bold'),
    fg_color="grey",
    width=100,
    height=40,
    corner_radius=10,
    hover_color="pink",
    text_color="orange",
    command=cart  # Corrected the command parameter
)
add_S.place(x=1150, y=35)

# redirecting

def snacks():
    os.system('python windows\\snacks.py')
def veg():
    os.system('python windows\\veg.py')
def nonveg():
    os.system('python windows\\nonveg.py')
def drinks():
    os.system('python windows\\drinks.py')
def cart():
    os.system('python windows\\cart.py')

# Load and display an image on the main frame
image_path = 'windows/images/aq11.jpg'  # Specify the path to your image
if os.path.exists(image_path):
    img = Image.open(image_path)
    img = img.resize((1300, 600))
    img = ImageTk.PhotoImage(img)
    img_label = ct.CTkLabel(main_f, image=img)
    img_label.image = img
    img_label.pack(pady=20)

s.mainloop()
