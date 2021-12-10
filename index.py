from tkinter import *
from tkinter import messagebox
from tkinter import ttk

win = Tk()
win.title("login system")
win.geometry("600x300")
win.configure(bg="white")
win.resizable(width=False, height=False)
win.attributes("-alpha", 0.9)
win.iconbitmap("LogoIcon.ico")

leftframe = Frame(win, width=200, height=300, bg="lightblue", relief="raise")
leftframe.pack(side="left")

rightframe = Frame(win, width=395, height=300, bg="gray", relief="raise")
rightframe.pack(side="right")

logo = PhotoImage(file="logo.png")
logolabel = Label(leftframe, image=logo, bg="lightblue")
logolabel.place(x=50, y=100)

userlabel = Label(rightframe, text="user:", font=("Arial", 15), background="gray", foreground="white")
userlabel.place(x=10, y=20)

userentry = ttk.Entry(rightframe, width=30)
userentry.place(x=150, y=20)

passwordlabel = Label(rightframe, text="password:", font=("Arial", 15), background="gray", foreground="white")
passwordlabel.place(x=10, y=50)

passwordentry = ttk.Entry(rightframe, width=30,show="*")
passwordentry.place(x=150, y=50)

loginbutton = ttk.Button(rightframe, text="login", width=10)
loginbutton.place(x=10, y=200)

regbutton = ttk.Button(rightframe, text="register", width=10)
regbutton.place(x=100, y=200)

win.mainloop()