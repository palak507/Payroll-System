import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def loan_show_scr():
    t=tkinter.Tk()
    t.geometry('700x600')
    t.title('EMPLOYEE LOAN DATA')
    t.configure(bg='cyan2')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=80, height=30, bg='cyan4', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        ls=''
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,dept_id,loan_amount from emp_loan_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            ls=ls+'\n '+str(res[0])+'\t'+str(res[1])+'\t'+str(res[2])
        b.insert(END, ls)

    filldata()
    t.mainloop()