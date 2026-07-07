import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def leave_show_scr():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('EMPLOYEE LEAVE DATA')
    t.configure(bg='gold2')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=80, height=30, bg='yellow', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        lt=''
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,month,no_of_leaves,type from emp_leave_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt=lt+'\n'+str(res[0])+'\t'+res[1]+'\t'+res[2]+'\t'+res[3]
        b.insert(END, lt)

    filldata()
    t.mainloop()