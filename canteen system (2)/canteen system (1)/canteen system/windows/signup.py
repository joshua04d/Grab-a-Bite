from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
import os

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')
    else:
        try:
            con = sqlite3.connect('userdata.db')
            cursor = con.cursor()
        except sqlite3.Error as e:
            messagebox.showerror('Error', f'Database Connectivity Issue: {e}')
            return
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT NOT NULL,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL)''')
        
        query = 'SELECT * FROM data WHERE username=?'
        cursor.execute(query, (usernameEntry.get(),))

        row = cursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already exists')
        else:
            query = 'INSERT INTO data (email, username, password) VALUES (?, ?, ?)'
            cursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
            signup_window.destroy()
            

def login_page():
    signup_window.destroy()
 

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)
background = ImageTk.PhotoImage(file='windows/images/background.jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=454, y=80)

heading = Label(frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 18, 'bold'), bg='white', fg='cadet blue')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='cadet blue')
emailLabel.grid(row=1, column=0, sticky='w', padx=25)

emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='cadet blue')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei VI Light', 10, 'bold'), bg='white', fg='cadet blue')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='cadet blue')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='cadet blue')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='cadet blue')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahed UI Light', 10, 'bold'), bg='white', fg='cadet blue')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

confirmEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='cadet blue')
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)
check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions', font=('Microsoft Yahei UI Light', 9, 'bold'),
                                 fg='cadet blue', bg='white', activebackground='white', activeforeground='firebrick',
                                 cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=15)

def admin():
    os.system('python windows\\admin.py')
    
signupButton = Button(frame, text='Signup', font=('0', 16, 'bold'), bd=0, bg='cadet blue', fg='white',
                      activebackground='firebrick1', activeforeground='white', width=17, command=lambda:admin())
signupButton.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'), bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton = Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'), bg='white', fg='blue', bd=0,
                     cursor='hand2', activebackground='white', activeforeground='blue', command=lambda:admin())


    
loginButton.place(x=170, y=387)

signup_window.mainloop()
