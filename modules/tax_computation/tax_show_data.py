import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
from database.mysql_connector import get_connection

def tax_show_scr():
    t=tkinter.Tk()
    t.geometry('800x600')
    t.title('TAX COMPUTATION DATA')
    t.configure(bg='red2')

    frame=Frame(t)
    frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    scrollbar=Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b=Text(frame, width=90, height=30, bg='tomato', yscrollcommand=scrollbar.set)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        tc=''
        db=get_connection()
        cur=db.cursor()
        sql="select emp_id,dept_id,CTC,tax_comp_per_month,net_amount from tax_computation"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            tc=tc+'\n'+str(res[0])+'\t'+str(res[1])+'\t'+res[2]+'\t'+res[3]+'\t'+res[4]
        b.insert(END, tc)

    filldata()
    t.mainloop()