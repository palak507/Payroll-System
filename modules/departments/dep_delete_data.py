import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from tkinter import ttk
from database.mysql_connector import get_connection
def dep_delete_scr():
    t=tkinter.Tk()
    t.geometry('800x800')
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
        
    def deletedata():
        db=get_connection()
        cur=db.cursor()
        xa=int(b.get())
        sql="delete from department where dept_id=%d"%(xa)
        cur.execute(sql)
        b.delete(0,100)
        messagebox.showinfo('Hi','Deleted')
        db.commit()
        db.close()
    def cm():
        t.destroy()
    
    aa=Label(t,text='DELETE DATA',font=('algerian',25),bg='violetred1')
    aa.place(x=200,y=50)    
    a=Label(t,text='Dept id',bg='violetred1')
    a.place(x=50,y=100)
    b=ttk.Combobox(t,width=20)
    filldata()
    b['values']=xt
    b.place(x=400,y=100)
    d=Button(t,text='Delete',command=deletedata,bg='violetred1')
    d.place(x=100,y=200)
    m=Button(t,text='Close',command=cm,bg='violetred1')
    m.place(x=250,y=200)
    t.mainloop()
