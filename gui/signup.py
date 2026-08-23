import tkinter
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import os
from dotenv import load_dotenv
from database.mysql_connector import get_connection

load_dotenv()

def signup_scr():
    t = ttkb.Toplevel()
    t.geometry('500x600')
    t.title('New Sign Up')

    def mail_otp():
        global otp
        e = d1.get()
        from_address = os.getenv("EMAIL_ADDRESS")
        to_address = e

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "OTP for new admin signup verification"
        msg['From'] = from_address
        msg['To'] = to_address

        otp = random.randint(100000, 999999)
        html = """The OTP for admin verification is %d""" % (otp)
        part1 = MIMEText(html, 'html')
        msg.attach(part1)

        username = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_PASSWORD")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        messagebox.showinfo('Hi', 'OTP SENT')

    def clr():
        a1.delete(0, END)
        b1.delete(0, END)
        d1.delete(0, END)
        e1.delete(0, END)

    def cm():
        t.destroy()

    def lgn():
        ot = int(e1.get())
        if ot == otp:
            db = get_connection()
            cur = db.cursor()
            xa = a1.get()
            xb = b1.get()
            xc = d1.get()
            sql = "insert into admins values ('%s','%s','%s')" % (xa, xb, xc)
            cur.execute(sql)
            db.commit()
            a1.delete(0, END)
            b1.delete(0, END)
            d1.delete(0, END)
            e1.delete(0, END)
            messagebox.showinfo('hi', 'New Admin Created')
        else:
            messagebox.showerror('error', 'Wrong OTP')

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="NEW ADMIN SIGNUP", font=('Segoe UI', 20, 'bold'), bootstyle="info").pack(pady=(10, 25))

    ttkb.Label(main_frame, text="New Username", font=('Segoe UI', 11)).pack(anchor=W, pady=(0, 4))
    a1 = ttkb.Entry(main_frame, width=35, bootstyle="info")
    a1.pack(pady=(0, 12))

    ttkb.Label(main_frame, text="Set Password", font=('Segoe UI', 11)).pack(anchor=W, pady=(0, 4))
    b1 = ttkb.Entry(main_frame, width=35, show='*', bootstyle="info")
    b1.pack(pady=(0, 12))

    ttkb.Label(main_frame, text="Email ID", font=('Segoe UI', 11)).pack(anchor=W, pady=(0, 4))
    d1 = ttkb.Entry(main_frame, width=35, bootstyle="info")
    d1.pack(pady=(0, 12))

    ttkb.Label(main_frame, text="Enter OTP", font=('Segoe UI', 11)).pack(anchor=W, pady=(0, 4))
    e1 = ttkb.Entry(main_frame, width=35, bootstyle="info")
    e1.pack(pady=(0, 20))

    ttkb.Button(main_frame, text="SEND OTP", bootstyle="warning", width=20, command=mail_otp).pack(pady=(0, 15))

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.pack()
    ttkb.Button(btn_frame, text="Verify OTP", bootstyle="success", width=12, command=lgn).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Clear", bootstyle="secondary", width=12, command=clr).grid(row=0, column=1, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=2, padx=5)

    t.mainloop()