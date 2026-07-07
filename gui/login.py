import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from gui.dashboardf import *
from gui.signup import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from database.mysql_connector import get_connection
t=tkinter.Toplevel()
t.protocol("WM_DELETE_WINDOW", lambda: exit())
t.geometry('800x800')
t.title('Login Page')
def clr():
    a1.delete(0,100)
    b1.delete(0,100)
def cm():
    exit()
def lgn():
    db=get_connection()
    cur=db.cursor()
    xa=a1.get()
    xb=b1.get()
    sql="select password from admins where username='%s'"%(xa)
    cur.execute(sql)
    data=cur.fetchone()
    pw=data[0]
    if xb==pw:
        a1.delete(0,100)
        b1.delete(0,100)
        t.withdraw()
        dashbrd(t)
    else:
        messagebox.showerror('Error','Invalid Login Credentials')
    a1.delete(0,100)
    b1.delete(0,100)    
    
x=Canvas(t,height=800,width=800,bg='lightblue')
x.place(x=1,y=1)
aa=Label(t,text='ADMIN LOGIN PAGE',font=('algerian',25),fg='blue',bg='lightblue')
aa.place(x=250,y=50)
a=Label(t,text='USER NAME',font=('Calibri',15,'bold'),fg='blue',bg='lightblue')
a.place(x=100,y=150)
a1=Entry(t,width=30)
a1.place(x=350,y=150)
b=Label(t,text='PASSWORD',font=('Calibri',15,'bold'),fg='blue',bg='lightblue')
b.place(x=100,y=250)
b1=Entry(t,width=30,show='*')
b1.place(x=350,y=250)
d=Button(t,text='Login',bg='blue',fg='lightblue',command=lgn)
d.place(x=250,y=320)
f=Button(t,text='Clear',bg='blue',fg='lightblue',command=clr)
f.place(x=350,y=320)
g=Button(t,text='Close',bg='blue',fg='lightblue',command=cm)
g.place(x=450,y=320)
st=Label(t,text='New User?...',font=('Calibri',12,'bold'),fg='blue',bg='lightblue')
st.place(x=250,y=360)
s=Button(t,text='SIGNUP',bg='blue',fg='lightblue',command=signup_scr)
s.place(x=350,y=360)
t.mainloop()