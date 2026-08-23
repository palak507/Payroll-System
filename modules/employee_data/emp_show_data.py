import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from database.mysql_connector import get_connection

def emp_show_data():
    t = ttkb.Toplevel()
    t.title('EMPLOYEE DATA')

    theme_bg = Style().colors.bg
    theme_fg = Style().colors.fg

    frame = ttkb.Frame(t, padding=15)
    frame.pack(fill=BOTH, expand=True)

    scrollbar = ttkb.Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b = Text(frame, width=100, height=30, bg=theme_bg, fg=theme_fg,
             insertbackground=theme_fg, yscrollcommand=scrollbar.set, relief=FLAT)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        et = ''
        db = get_connection()
        cur = db.cursor()
        sql = "select emp_id,name,address,phone_no,doj,designation,dept_id from emp_data order by emp_id"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            et = et + '\n ' + str(res[0]) + '\t' + res[1] + '\t' + res[2] + '\t' + (res[3] + '\t' + str(res[4]) + '\t' + (res[5]) + '\t' + str(res[6]))
        b.insert(END, et)

    filldata()

    t.geometry('900x600')
    t.mainloop()