import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def tax_upd_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='red2')
    x.place(x=1,y=1)
    
    xt=[]
    
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id from tax_computation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
     
    def finddata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        sql="select dept_id,CTC,tax_comp_per_month,net_amount from tax_computation where emp_id=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        d1.delete(0,100)
        g1.delete(0,100)
        j1.delete(0,100)
        e1.delete(0,100)
        d1.insert(0,data[0])
        g1.insert(0,data[1])
        j1.insert(0,data[2])
        e1.insert(0,data[3])
        db.close()
    
    def update():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        xb=int(d1.get())
        xc=g1.get()
        xd=j1.get()
        xe=e1.get()
        sql="update tax_computation set dept_id=%d,CTC='%s',tax_comp_per_month='%s',net_amount='%s' where emp_id    =%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi','Updated')
        d1.delete(0,100)
        g1.delete(0,100)
        j1.delete(0,100)
        e1.delete(0,100)
        db.close()
    
    
    def cm():
            t.destroy()
    
       
    aa=Label(t,text='UPDATE DATA',font=('algerian',25),bg='tomato')
    aa.place(x=250,y=60) 
    b=Label(t,text='Empid',font=12,bg='tomato')
    b.place(x=130,y=150)
    b1=ttk.Combobox(t)
    b1.place(x=300,y=150)
    filldata()
    b1['values']=xt
    
    m=Button(t,text='Find',command=finddata,bg='tomato')
    m.place(x=300,y=200)
    
    d=Label(t,text='Dept id',font=12,bg='tomato')
    d.place(x=130,y=250)
    d1=Entry(t,width=20)
    d1.place(x=300,y=250)
    
    g=Label(t,text='CTC',font=12,bg='tomato')
    g.place(x=130,y=300)
    g1=Entry(t,width=20)
    g1.place(x=300,y=300)
    
    j=Label(t,text='Tax Comp Per Month',font=12,bg='tomato')
    j.place(x=130,y=350)
    j1=Entry(t,width=20)
    j1.place(x=300,y=350)
    
    e=Label(t,text='Net Amount',font=12,bg='tomato')
    e.place(x=130,y=400)
    e1=Entry(t,width=20)
    e1.place(x=300,y=400)
    
    m1=Button(t,text='Close',command=cm,bg='tomato')
    m1.place(x=350,y=450)
    n=Button(t,text='Update',command=update,bg='tomato')
    n.place(x=250,y=450)
    
    t.mainloop()
