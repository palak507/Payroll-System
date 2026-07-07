import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def loan_upd_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='cyan2')
    x.place(x=1,y=1)
    xt=[]
    
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id from emp_loan_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    
    def finddata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        sql="select dept_id,loan_amount from emp_loan_data where emp_id=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        d1.delete(0,100)
        g1.delete(0,100)
        d1.insert(0,data[0])
        g1.insert(0,data[1])
        db.close()
        
    def update():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        xb=int(d1.get())
        xc=int(g1.get())
        sql="update emp_loan_data set dept_id=%d,loan_amount=%d where emp_id=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Updated')
        d1.delete(0,100)
        g1.delete(0,100)
        db.close()
    
    
    def cm():
            t.destroy()
    
    aa=Label(t,text='UPDATE DATA',font=('algerian',25),bg='cyan4')
    aa.place(x=250,y=60)
    b=Label(t,text='Empid',font=12,bg='cyan4')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t)
    b1.place(x=300,y=150)
    filldata()
    b1['values']=xt
    
    m=Button(t,text='Find',command=finddata,bg='cyan4')
    m.place(x=300,y=200)
    
    d=Label(t,text='Deptid',font=12,bg='cyan4')
    d.place(x=150,y=250)
    d1=Entry(t,width=20)
    d1.place(x=300,y=250)
    
    g=Label(t,text='Loan Amount',font=12,bg='cyan4')
    g.place(x=130,y=300)
    g1=Entry(t,width=20)
    g1.place(x=300,y=300)
    
    m1=Button(t,text='Update',command=update,bg='cyan4')
    m1.place(x=250,y=400)
    
    
    m2=Button(t,text='Close',command=cm,bg='cyan4')
    m2.place(x=350,y=400)
    
    
    t.mainloop()