import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def salcom_show_scr():
    t=tkinter.Tk()
    t.geometry('800x600')
    t.title('SALARY COMPUTATION DATA')
    t.configure(bg='purple3')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=90, height=30, bg='mediumpurple1', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        sc=''
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,dept_id,month,net_payable from salary_computation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            sc=sc+'\n'+str(res[0])+'\t'+str(res[1])+'\t'+res[2]+'\t'+res[3]
        b.insert(END, sc)

    filldata()
    t.mainloop()