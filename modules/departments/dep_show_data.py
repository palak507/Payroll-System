import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def dep_show_scr():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('DEPARTMENT DATA')
    t.configure(bg='pink')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=80, height=30, bg='violetred1', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        dt=' '
        db=get_connection()
        cur=db.cursor()
        sql="select dept_id,dept_name,HOD from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            dt=dt+'\n'+str(res[0])+'\t'+str(res[1])+'\t'+str(res[2])
        b.insert(END, dt)

    filldata()
    t.mainloop()