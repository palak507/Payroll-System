import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def emp_show_data():
    t=tkinter.Tk()
    t.geometry('900x600')
    t.title('EMPLOYEE DATA')
    t.configure(bg='forestgreen')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=100, height=30, bg='lightgreen', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        et=''
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,name,address,phone_no,doj,designation,dept_id from emp_data"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            et=et+'\n '+str(res[0])+'\t'+res[1]+'\t'+res[2]+'\t'+(res[3]+'\t'+str(res[4])+'\t'+(res[5])+'\t'+str(res[6]))
        b.insert(END, et)

    filldata()
    t.mainloop()