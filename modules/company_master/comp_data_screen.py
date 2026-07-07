import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection
def comp_data_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Show Data')
    x=Canvas(t,height=800,width=800,bg='salmon1')
    x.place(x=1,y=1)
    
    xa=[]
    xb=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    
    i=0
    
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select comp_id,name,address,email,phone_no,reg_no from comp_master"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xd.append(res[2])
            xe.append(res[3])
            xf.append(res[4])
            xg.append(res[5])
        db.close()
    def firstrecord():
        global i
        i=0
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
    def nextrecord():
        global i
        i=i+1
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
    def prevrecord():
        global i
        i=i-1
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
    def lastrecord():
        global i
        i=len(xa)-1
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
    def cm():
        t.destroy()
    
    aa=Label(t,text='VIEW DATA',font=('algerian',25),bg='salmon1')
    aa.place(x=250,y=60)
    a=Label(t,text='Comp Id',font=('arial',20,'bold'),bg='salmon1')
    a.place(x=80,y=130)
    a1=Entry(t,width=40)
    a1.place(x=330,y=140)
    
    b=Label(t,text='Name',font=('arial',20,'bold'),bg='salmon1')
    b.place(x=80,y=190)
    b1=Entry(t,width=40)
    b1.place(x=330,y=205)
    
    d=Label(t,text='Address',font=('arial',20,'bold'),bg='salmon1')
    d.place(x=80,y=255)
    d1=Entry(t,width=40)
    d1.place(x=330,y=270)
    
    e=Label(t,text='Email',font=('arial',20,'bold'),bg='salmon1')
    e.place(x=80,y=325)
    e1=Entry(t,width=40)
    e1.place(x=330,y=335)
    
    f=Label(t,text='Phone No.',font=('arial',20,'bold'),bg='salmon1')
    f.place(x=80,y=380)
    f1=Entry(t,width=40)
    f1.place(x=330,y=390)
    
    g=Label(t,text='Reg No.',font=('arial',20,'bold'),bg='salmon1')
    g.place(x=80,y=425)
    g1=Entry(t,width=40)
    g1.place(x=330,y=435)
    
    
    bt=Button(t,text='First',font=('arial',15,'bold'),bg='peachpuff',bd=5,command=firstrecord)
    bt.place(x=100,y=480)
    
    bt1=Button(t,text='Next',font=('arial',15,'bold'),bg='peachpuff',bd=5,command=nextrecord)
    bt1.place(x=300,y=480)
    
    bt2=Button(t,text='Last',font=('arial',15,'bold'),bg='peachpuff',bd=5,command=lastrecord)
    bt2.place(x=450,y=480)
    
    bt3=Button(t,text='Previous',font=('arial',15,'bold'),bg='peachpuff',bd=5,command=prevrecord)
    bt3.place(x=600,y=480)
    filldata()
    
    c1=Button(t,text='Close',font=('arial',15,'bold'),bg='peachpuff',bd=5,command=cm)
    c1.place(x=400,y=550)
    
    t.mainloop()
