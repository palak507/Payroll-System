import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def emp_del_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
    x=Canvas(t,height=800,width=800,bg='forestgreen')
    x.place(x=1,y=1)
    xt=[]
    def filldata():
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id from emp_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()
    def cm():
        t.destroy()
        
    def deletedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b.get())
        sql="delete from emp_data where emp_id=%d"%(xa)
        cur.execute(sql)
        b.delete(0,100)
        messagebox.showinfo('Hi','Deleted')
        db.commit()
        db.close()
    
    aa=Label(t,text='DELETE DATA',font=('algerian',25),bg='lightgreen')
    aa.place(x=170,y=50)
    a=Label(t,text='Emp id',bg='lightgreen')
    a.place(x=50,y=100)
    b=ttk.Combobox(t,width=20)
    filldata()
    b['values']=xt
    b.place(x=400,y=100)
    d=Button(t,text='Delete',command=deletedata,bg='lightgreen')
    d.place(x=100,y=200)
    p=Button(t,text='Close',command=cm,bg='lightgreen')
    p.place(x=200,y=200)
    t.mainloop()