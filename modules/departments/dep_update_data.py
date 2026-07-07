import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def dep_update_scr():
        
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('DEPARTMENT DATA UPDATE')
    x=Canvas(t,height=800,width=800,bg='pink')
    x.place(x=1,y=1)
    xt=[]
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select dept_id from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b.get())
        sql="select dept_name,HOD from department where dept_id=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        f.delete(0,100)
        h.delete(0,100)
        f.insert(0,data[0])
        h.insert(0,data[1])
    def update():
        db=get_connection()
        cur=db.cursor()
        xa=int(b.get())
        xb=f.get()
        xc=h.get()
        sql="update department set dept_name='%s',HOD='%s' where dept_id=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Updated')
        b.delete(0,100)
        f.delete(0,100)
        h.delete(0,100)
        db.close()
    def cm():
        t.destroy()
        
    aa=Label(t,text='UPDATE DATA',font=('algerian',25),bg='violetred1')
    aa.place(x=200,y=50)
    a=Label(t,text='Dept id',bg='violetred1')
    a.place(x=50,y=100)
    b=ttk.Combobox(t,width=20)
    filldata()
    b['values']=xt
    b.place(x=400,y=100)
    d=Button(t,text='Find',command=finddata,bg='violetred1')
    d.place(x=250,y=140)
    e=Label(t,text='New Dept Name',bg='violetred1')
    e.place(x=50,y=180)
    f=Entry(t,width=20)
    f.place(x=400,y=180)
    g=Label(t,text='New HOD',bg='violetred1')
    g.place(x=50,y=220)
    h=Entry(t,width=20)
    h.place(x=400,y=220)
    v=Button(t,text='Update',command=update,bg='violetred1')
    v.place(x=250,y=300)
    w=Button(t,text='Close',command=cm,bg='violetred1')
    w.place(x=350,y=300)
    
    t.mainloop()
