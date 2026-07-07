import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from database.mysql_connector import get_connection
def dep_insert_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='pink')
    x.place(x=1,y=1)
    def savedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b.get())
        xb=e.get()
        xc=g.get()
        sql="insert into department values(%d,'%s','%s')"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        b.delete(0,100)
        e.delete(0,100)
        g.delete(0,100)
        db.close()
        messagebox.showinfo('Hi','Saved')
    def cm():
        t.destroy()
    aa=Label(t,text='INSERT DATA',font=('algerian',25),bg='violetred1')
    aa.place(x=200,y=50)    
    a=Label(t,text='Department id',bg='violetred1')
    a.place(x=50,y=100)
    b=Entry(t,width=20)
    b.place(x=400,y=100)
    d=Label(t,text='Department name',bg='violetred1')
    d.place(x=50,y=140)
    e=Entry(t,width=20)
    e.place(x=400,y=140)
    f=Label(t,text='HOD',bg='violetred1')
    f.place(x=50,y=180)
    g=Entry(t,width=20)
    g.place(x=400,y=180)
    r=Button(t,text='Save',command=savedata,bg='violetred1')
    r.place(x=250,y=250)
    u=Button(t,text='Close',command=cm,bg='violetred1')
    u.place(x=350,y=250)
    
    t.mainloop()
