import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from database.mysql_connector import get_connection
def leave_ins_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='gold2')
    x.place(x=1,y=1)
    def savedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        xb=(d1.get())
        xc=(g1.get())
        xd=(j1.get())
        sql="insert into emp_leave_data values(%d,'%s','%s','%s')"%(xa,xb,xc,xd)
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
    
    aa=Label(t,text='INSERT DATA',font=('algerian',25),bg='yellow')
    aa.place(x=250,y=60)
    b=Label(t,text='Empid',font=12,bg='yellow')
    b.place(x=150,y=150)
    b1=Entry(t,width=20)
    b1.place(x=300,y=150)
    
    d=Label(t,text='Month',font=12,bg='yellow')
    d.place(x=150,y=200)
    d1=Entry(t,width=20)
    d1.place(x=300,y=200)
    
    g=Label(t,text='No. of leaves',font=12,bg='yellow')
    g.place(x=130,y=250)
    g1=Entry(t,width=20)
    g1.place(x=300,y=250)
    
    j=Label(t,text='Type',font=12,bg='yellow')
    j.place(x=150,y=300)
    j1=Entry(t,width=20)
    j1.place(x=300,y=300)
    
    
    m=Button(t,text='Save',command=savedata,bg='yellow')
    m.place(x=250,y=400)
    m1=Button(t,text='Close',command=cm,bg='yellow')
    m1.place(x=350,y=400)
    
    t.mainloop()