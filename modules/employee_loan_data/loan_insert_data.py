import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from database.mysql_connector import get_connection
def loan_ins_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='cyan2')
    x.place(x=1,y=1)
    def savedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        xb=int(d1.get())
        xc=int(g1.get())
        sql="insert into emp_loan_data values(%d,%d,%d)"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        b1.delete(0,100)
        d1.delete(0,100)
        g1.delete(0,100)
        db.close()
        messagebox.showinfo('Hi','Saved')
    
    def cm():
        t.destroy()
    
    aa=Label(t,text='INSERT DATA',font=('algerian',25),bg='cyan4')
    aa.place(x=250,y=60)
    b=Label(t,text='Empid',font=12,bg='cyan4')
    b.place(x=150,y=150)
    b1=Entry(t,width=20)
    b1.place(x=300,y=150)
    
    d=Label(t,text='Deptid',font=12,bg='cyan4')
    d.place(x=150,y=200)
    d1=Entry(t,width=20)
    d1.place(x=300,y=200)
    
    g=Label(t,text='Loan Amount ',font=12,bg='cyan4')
    g.place(x=130,y=250)
    g1=Entry(t,width=20)
    g1.place(x=300,y=250)
    
    
    m=Button(t,text='Save',command=savedata,bg='cyan4')
    m.place(x=250,y=350)
    m1=Button(t,text='Close',command=cm,bg='cyan4')
    m1.place(x=350,y=350)
    
    t.mainloop()