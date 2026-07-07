import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection
def emp_data_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    t.title('Show Data ')
    x=Canvas(t,height=800,width=800,bg='forestgreen')
    x.place(x=1,y=1)
    
    xa=[]
    xb=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    xh=[]
    
    i=0
    
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,name,address,phone_no,doj,designation,dept_id from emp_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xd.append(res[2])
            xe.append(res[3])
            xf.append(res[4])
            xg.append(res[5])
            xh.append(res[6])
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
        h1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
        h1.insert(0,str(xh[i]))
    def nextrecord():
        global i
        i=i+1
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        h1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
        h1.insert(0,str(xh[i]))
    def prevrecord():
        global i
        i=i-1
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        h1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
        h1.insert(0,str(xh[i]))
    def lastrecord():
        global i
        i=len(xa)-1
        a1.delete(0,100)
        b1.delete(0,100)
        d1.delete(0,100)
        e1.delete(0,100)
        f1.delete(0,100)
        g1.delete(0,100)
        h1.delete(0,100)
        a1.insert(0,str(xa[i]))
        b1.insert(0,xb[i])
        d1.insert(0,xd[i])
        e1.insert(0,xe[i])
        f1.insert(0,xf[i])
        g1.insert(0,xg[i])
        h1.insert(0,str(xh[i]))

    def cm():
        t.destroy()
    
    aa=Label(t,text='VIEW DATA',font=('algerian',25),bg='lightgreen')
    aa.place(x=250,y=60)
    
    a=Label(t,text='Emp Id',font=('arial',20,'bold'),bg='lightgreen')
    a.place(x=80,y=130)
    a1=Entry(t,width=40)
    a1.place(x=330,y=140)
    
    b=Label(t,text='Name',font=('arial',20,'bold'),bg='lightgreen')
    b.place(x=80,y=200)
    b1=Entry(t,width=40)
    b1.place(x=330,y=215)
    
    d=Label(t,text='Address',font=('arial',20,'bold'),bg='lightgreen')
    d.place(x=80,y=270)
    d1=Entry(t,width=40)
    d1.place(x=330,y=285)
    
    e=Label(t,text='Phone no',font=('arial',20,'bold'),bg='lightgreen')
    e.place(x=80,y=340)
    e1=Entry(t,width=40)
    e1.place(x=330,y=350)
    
    f=Label(t,text='doj',font=('arial',20,'bold'),bg='lightgreen')
    f.place(x=80,y=380)
    f1=Entry(t,width=40)
    f1.place(x=330,y=390)
    
    g=Label(t,text='designation',font=('arial',20,'bold'),bg='lightgreen')
    g.place(x=80,y=420)
    g1=Entry(t,width=40)
    g1.place(x=330,y=430)

    h=Label(t,text='Dept Id',font=('arial',20,'bold'),bg='lightgreen')
    h.place(x=80,y=460)
    h1=Entry(t,width=40)
    h1.place(x=330,y=470)
    
    
    
    
    bt=Button(t,text='First',font=('arial',15,'bold'),bg='lightgreen',bd=5,command=firstrecord)
    bt.place(x=100,y=550)
    
    bt1=Button(t,text='Next',font=('arial',15,'bold'),bg='lightgreen',bd=5,command=nextrecord)
    bt1.place(x=300,y=550)
    
    bt2=Button(t,text='Last',font=('arial',15,'bold'),bg='lightgreen',bd=5,command=lastrecord)
    bt2.place(x=450,y=550)
    
    bt3=Button(t,text='Previous',font=('arial',15,'bold'),bg='lightgreen',bd=5,command=prevrecord)
    bt3.place(x=600,y=550)
    filldata()
    
    c1=Button(t,text='Close',font=('arial',15,'bold'),bg='lightgreen',bd=5,command=cm)
    c1.place(x=350,y=620)
    
    t.mainloop()
