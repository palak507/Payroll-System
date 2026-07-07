import tkinter
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import pymysql
from database.mysql_connector import get_connection
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file
def signup_scr():    
    t=tkinter.Toplevel()
    t.geometry('800x800')
    t.title('New Sign Up')
    def mail_otp():
        global otp
        e=d1.get()
        from_address =  os.getenv("EMAIL_ADDRESS")
        to_address = e
    
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "OTP for new admin signup verification"
        msg['From'] = from_address
        msg['To'] = to_address
    
        # create OTP
        otp=random.randint(100000,999999)
    
    
        # Create the message (HTML).
        html = """The OTP for admin verification is %d"""%(otp)
    
        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')
    
        # Attach parts into message container
        msg.attach(part1)
    
        # Credentials
        username = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_PASSWORD")
    
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        messagebox.showinfo('Hi','OTP SENT')
    def clr():
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
    def cm():
        t.destroy()
    def lgn():
        ot=int(e1.get())
        if ot==otp:
            
            db=get_connection()
            cur=db.cursor()
            xa=a1.get()
            xb=b1.get()
            xc=d1.get()
            sql="insert into admins values ('%s','%s','%s')"%(xa,xb,xc)
            cur.execute(sql)
            db.commit()
            a1.delete(0,100)
            b1.delete(0,100)
            d1.delete(0,100)
            e1.delete(0,100)
            messagebox.showinfo('hi','New Admin Created')
        else:
            messagebox.showerror('error','Wrong OTP')
        
    x=Canvas(t,height=800,width=800,bg='steelblue')
    x.place(x=1,y=1)
    aa=Label(t,text='NEW ADMIN SIGNUP ',font=('algerian',25),fg='white',bg='steelblue')
    aa.place(x=250,y=50)
    a=Label(t,text='NEW USER NAME',font=('Calibri',15,'bold'),fg='white',bg='steelblue')
    a.place(x=100,y=150)
    a1=Entry(t,width=30)
    a1.place(x=350,y=150)
    b=Label(t,text='SET PASSWORD',font=('Calibri',15,'bold'),fg='white',bg='steelblue')
    b.place(x=100,y=200)
    b1=Entry(t,width=30,show='*')
    b1.place(x=350,y=200)
    d=Label(t,text='ENTER EMAIL ID',font=('Calibri',15,'bold'),fg='white',bg='steelblue')
    d.place(x=100,y=250)
    d1=Entry(t,width=30)
    d1.place(x=350,y=250)
    e=Label(t,text='ENTER OTP',font=('Calibri',15,'bold'),fg='white',bg='steelblue')
    e.place(x=100,y=300)
    e1=Entry(t,width=30)
    e1.place(x=350,y=300)
    h=Button(t,text='Verify OTP',bg='steelblue',fg='white',command=lgn)
    h.place(x=220,y=400)
    f=Button(t,text='Clear',bg='steelblue',fg='white',command=clr)
    f.place(x=350,y=400)
    g=Button(t,text='Close',bg='steelblue',fg='white',command=cm)
    g.place(x=450,y=400)
    k=Button(t,text='SEND OTP',bg='steelblue',fg='white',command=mail_otp)
    k.place(x=300,y=360)
    
    
    t.mainloop()