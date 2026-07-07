import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def comp_find_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='salmon1')
    x.place(x=1,y=1)
    xt=[]
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select comp_id from comp_master"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def finddata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b.get())
        sql="select name,address,email,phone_no,reg_no from comp_master where comp_id=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        f.delete(0,100)
        h.delete(0,100)
        m.delete(0,100)
        p.delete(0,100)
        u.delete(0,100)
        f.insert(0,data[0])
        h.insert(0,data[1])
        m.insert(0,data[2])
        p.insert(0,data[3])
        u.insert(0,str(data[4]))
        db.close()
    def cm():
        t.destroy()
    aa=Label(t,text='FIND DATA',font=('algerian',20),bg='salmon1')    
    aa.place(x=250,y=50)    
    a=Label(t,text='Company id',bg='salmon1')
    a.place(x=50,y=100)
    b=ttk.Combobox(t,width=20)
    filldata()
    b['values']=xt
    b.place(x=400,y=100)
    d=Button(t,text='Find',command=finddata,bg='peachpuff')
    d.place(x=200,y=140)
    e=Label(t,text='Name',bg='salmon1')
    e.place(x=50,y=180)
    f=Entry(t,width=20)
    f.place(x=400,y=180)
    g=Label(t,text='Address',bg='salmon1')
    g.place(x=50,y=220)
    h=Entry(t,width=20)
    h.place(x=400,y=220)
    k=Label(t,text='Email',bg='salmon1')
    k.place(x=50,y=260)
    m=Entry(t,width=20)
    m.place(x=400,y=260)
    n=Label(t,text='Phone no',bg='salmon1')
    n.place(x=50,y=300)
    p=Entry(t,width=20)
    p.place(x=400,y=300)
    r=Label(t,text='Registration no',bg='salmon1')
    r.place(x=50,y=340)
    u=Entry(t,width=20)
    u.place(x=400,y=340)
    v=Button(t,text='Close',command=cm,bg='peachpuff')
    v.place(x=200,y=400)
    
    
    t.mainloop()
