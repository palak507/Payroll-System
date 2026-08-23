import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from database.mysql_connector import get_connection

def salcom_show_scr():
    t = ttkb.Toplevel()
    t.title('SALARY COMPUTATION DATA')

    theme_bg = Style().colors.bg
    theme_fg = Style().colors.fg

    frame = ttkb.Frame(t, padding=15)
    frame.pack(fill=BOTH, expand=True)

    scrollbar = ttkb.Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b = Text(frame, width=90, height=30, bg=theme_bg, fg=theme_fg,
             insertbackground=theme_fg, yscrollcommand=scrollbar.set, relief=FLAT)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        sc = ''
        db = get_connection()
        cur = db.cursor()
        sql = "select emp_id,dept_id,month,net_payable from salary_computation order by emp_id"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            sc = sc + '\n' + str(res[0]) + '\t' + str(res[1]) + '\t' + res[2] + '\t' + res[3]
        b.insert(END, sc)

    filldata()

    t.geometry('800x600')
    t.mainloop()