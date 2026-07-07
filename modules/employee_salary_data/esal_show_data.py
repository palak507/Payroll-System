import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def esal_show_scr():
    t=tkinter.Tk()
    t.geometry('800x600')
    t.title('EMPLOYEE SALARY DATA')
    t.configure(bg='darkorange')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=90, height=30, bg='orangered2', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        es=''
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,ctc,variable_pay,slab,grade from emp_salary_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            es=es+'\n'+str(res[0])+'\t'+res[1]+'\t'+res[2]+'\t'+res[3]+'\t'+res[4]
        b.insert(END, es)

    filldata()
    t.mainloop()