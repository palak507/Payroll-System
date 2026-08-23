import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from database.mysql_connector import get_connection

def dep_show_scr():
    t = ttkb.Toplevel()
    t.title('DEPARTMENT DATA')

    theme_bg = Style().colors.bg
    theme_fg = Style().colors.fg

    frame = ttkb.Frame(t, padding=15)
    frame.pack(fill=BOTH, expand=True)

    scrollbar = ttkb.Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    b = Text(frame, width=80, height=30, bg=theme_bg, fg=theme_fg,
             insertbackground=theme_fg, yscrollcommand=scrollbar.set, relief=FLAT)
    b.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=b.yview)

    def filldata():
        dt = ' '
        db = get_connection()
        cur = db.cursor()
        sql = "select dept_id,dept_name,HOD from department"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            dt = dt + '\n' + str(res[0]) + '\t' + str(res[1]) + '\t' + str(res[2])
        b.insert(END, dt)

    filldata()

    t.geometry('700x600')
    t.mainloop()