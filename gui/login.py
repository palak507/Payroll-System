import tkinter
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import pymysql
from database.mysql_connector import get_connection
from gui.dashboardf import *
from gui.signup import *

t = ttkb.Window(theme="nord-dark")
t.geometry('500x550')
t.title('Login Page')
t.protocol("WM_DELETE_WINDOW", exit)

def clr():
    a1.delete(0, END)
    b1.delete(0, END)

def cm():
    exit()

def lgn():
    db = get_connection()
    cur = db.cursor()
    xa = a1.get()
    xb = b1.get()
    sql = "select password from admins where username='%s'" % (xa)
    cur.execute(sql)
    data = cur.fetchone()
    if data is None:
        messagebox.showerror('Error', 'Invalid Login Credentials')
        return
    pw = data[0]
    if xb == pw:
        a1.delete(0, END)
        b1.delete(0, END)
        t.withdraw()
        dashbrd(t)
    else:
        messagebox.showerror('Error', 'Invalid Login Credentials')

main_frame = ttkb.Frame(t, padding=30)
main_frame.pack(expand=True, fill=BOTH)

title = ttkb.Label(main_frame, text="ADMIN LOGIN", font=('Segoe UI', 22, 'bold'), bootstyle="info")
title.grid(row=0, column=0, columnspan=2, pady=(10, 30))

ttkb.Label(main_frame, text="Username", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
a1 = ttkb.Entry(main_frame, width=28, bootstyle="info")
a1.grid(row=1, column=1, pady=8)

ttkb.Label(main_frame, text="Password", font=('Segoe UI', 11)).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 15))
b1 = ttkb.Entry(main_frame, width=28, show='*', bootstyle="info")
b1.grid(row=2, column=1, pady=8)

btn_frame = ttkb.Frame(main_frame)
btn_frame.grid(row=3, column=0, columnspan=2, pady=(25, 10))

ttkb.Button(btn_frame, text="Login", bootstyle="success", width=12, command=lgn).grid(row=0, column=0, padx=5)
ttkb.Button(btn_frame, text="Clear", bootstyle="secondary", width=12, command=clr).grid(row=0, column=1, padx=5)
ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=2, padx=5)

signup_frame = ttkb.Frame(main_frame)
signup_frame.grid(row=4, column=0, columnspan=2, pady=(30, 0))
ttkb.Label(signup_frame, text="New User?", font=('Segoe UI', 10)).pack(side=LEFT, padx=(0, 8))
ttkb.Button(signup_frame, text="SIGNUP", bootstyle="info-outline", command=signup_scr).pack(side=LEFT)

t.mainloop()