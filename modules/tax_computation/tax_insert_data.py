import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from database.mysql_connector import get_connection
def tax_ins_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='red2')
    x.place(x=1,y=1)
    
    
    def savedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        xb=int(d1.get())
        xc=g1.get()
        xd=j1.get()
        xe=e1.get()
        sql="insert into tax_computation values(%d,%d,'%s','%s','%s')"%(xa,xb,xc,xd,xe)
        cur.execute(sql)
        db.commit()
        b1.delete(0,100)
        d1.delete(0,100)
        g1.delete(0,100)
        j1.delete(0,100)
        e1.delete(0,100)
        db.close()
        messagebox.showinfo('hi','saved')
    
    def cm():
        t.destroy()
    
    aa=Label(t,text='INSERT DATA',font=('algerian',25),bg='tomato')
    aa.place(x=250,y=60)
    b=Label(t,text='Empid',font=12,bg='tomato')
    b.place(x=130,y=150)
    b1=Entry(t,width=20)
    b1.place(x=300,y=150)
    
    d=Label(t,text='Dept id',font=12,bg='tomato')
    d.place(x=130,y=200)
    d1=Entry(t,width=20)
    d1.place(x=300,y=200)
    
    g=Label(t,text='CTC',font=12,bg='tomato')
    g.place(x=130,y=250)
    g1=Entry(t,width=20)
    g1.place(x=300,y=250)
    
    j=Label(t,text='Tax Comp Per Month',font=12,bg='tomato')
    j.place(x=130,y=300)
    j1=Entry(t,width=20)
    j1.place(x=300,y=300)
    
    e=Label(t,text='Net Amount',font=12,bg='tomato')
    e.place(x=130,y=350)
    e1=Entry(t,width=20)
    e1.place(x=300,y=350)
    
    m=Button(t,text='Save',command=savedata,bg='tomato')
    m.place(x=350,y=400)
    m1=Button(t,text='Close',command=cm,bg='tomato')
    m1.place(x=450,y=400)
    
    t.mainloop()
