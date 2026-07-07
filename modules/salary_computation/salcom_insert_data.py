import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from database.mysql_connector import get_connection
def salcom_ins_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='purple3')
    x.place(x=1,y=1)
    
    def savedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        xb=int(d1.get())
        xc=(g1.get())
        xd=(j1.get())
        sql="insert into salary_computation values(%d,%d,'%s','%s')"%(xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        b1.delete(0,100)
        d1.delete(0,100)
        g1.delete(0,100)
        j1.delete(0,100)
        db.close()
        messagebox.showinfo('hi','saved')
    
    def cm():
        t.destroy()
    
    aa=Label(t,text='INSERT DATA',font=('algerian',25),bg='mediumpurple1')
    aa.place(x=250,y=60)  
    b=Label(t,text='Empid',font=12,bg='mediumpurple1')
    b.place(x=150,y=150)
    b1=Entry(t,width=20)
    b1.place(x=300,y=150)
    
    d=Label(t,text='Dept id',font=12,bg='mediumpurple1')
    d.place(x=150,y=200)
    d1=Entry(t,width=20)
    d1.place(x=300,y=200)
    
    g=Label(t,text='Month',font=12,bg='mediumpurple1')
    g.place(x=150,y=250)
    g1=Entry(t,width=20)
    g1.place(x=300,y=250)
    
    j=Label(t,text='Net Payable',font=12,bg='mediumpurple1')
    j.place(x=150,y=300)
    j1=Entry(t,width=20)
    j1.place(x=300,y=300)
    
    
    m=Button(t,text='Save',command=savedata,bg='mediumpurple1')
    m.place(x=300,y=380)
    m1=Button(t,text='Close',command=cm,bg='mediumpurple1')
    m1.place(x=400,y=380)
    
    t.mainloop()
