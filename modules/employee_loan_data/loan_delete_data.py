import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def loan_del_scr():
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
        
    def deletedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b1.get())
        sql="delete from emp_loan_data where emp_id=%d"%(xa)
        cur.execute(sql)
        b1.delete(0,100)
        messagebox.showinfo('Hi','Deleted')
        db.commit()
        db.close()  
    def cm():
        t.destroy()
    aa=Label(t,text='DELETE DATA',font=('algerian',25),bg='cyan4')
    aa.place(x=250,y=60)
    b=Label(t,text='Empid',font=12,bg='cyan4')
    b.place(x=150,y=150)
    b1=ttk.Combobox(t)
    b1.place(x=300,y=150)
    filldata()
    b1['values']=xt
    
    n=Button(t,text='Delete',command=deletedata,bg='cyan4')
    n.place(x=250,y=200)
    p=Button(t,text='Close',command=cm,bg='cyan4')
    p.place(x=350,y=200)
    t.mainloop()