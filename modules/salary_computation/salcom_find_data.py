import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def salcom_find_scr():
        
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='purple3')
    x.place(x=1,y=1)
    xt=[]
    
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id from salary_computation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
     
    def finddata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        sql="select dept_id,month,net_payable from salary_computation where emp_id=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        d1.delete(0,100)
        g1.delete(0,100)
        j1.delete(0,100)
        d1.insert(0,data[0])
        g1.insert(0,data[1])
        j1.insert(0,data[2])
        db.close()
    def cm():
            t.destroy()
    
       
    aa=Label(t,text='FIND DATA',font=('algerian',25),bg='mediumpurple1')
    aa.place(x=250,y=60)  
    b=Label(t,text='Empid',font=12,bg='mediumpurple1')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t)
    b1.place(x=300,y=150)
    filldata()
    b1['values']=xt
    
    m=Button(t,text='Find',command=finddata,bg='mediumpurple1')
    m.place(x=300,y=200)
    
    d=Label(t,text='Dept id',font=12,bg='mediumpurple1')
    d.place(x=150,y=250)
    d1=Entry(t,width=20)
    d1.place(x=300,y=250)
    
    g=Label(t,text='Month',font=12,bg='mediumpurple1')
    g.place(x=150,y=300)
    g1=Entry(t,width=20)
    g1.place(x=300,y=300)
    
    j=Label(t,text='Net Payable',font=12,bg='mediumpurple1')
    j.place(x=150,y=350)
    j1=Entry(t,width=20)
    j1.place(x=300,y=350)
    
    
    m1=Button(t,text='Close',command=cm,bg='mediumpurple1')
    m1.place(x=300,y=450)
    
    t.mainloop()
