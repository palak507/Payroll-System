import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from database.mysql_connector import get_connection

def comp_show_scr():
    t = ttkb.Toplevel()
    t.title('COMPANY MASTER DATA')

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
        st = ''
        db = get_connection()
        cur = db.cursor()
        sql = "select comp_id,name,address,email,phone_no,reg_no from comp_master"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            st = st + '\n ' + str(res[0]) + '\t' + res[1] + '\t' + res[2] + '\t' + (res[3] + '\t' + res[4] + '\t' + str(res[5]))
        b.insert(END, st)

    filldata()

    t.geometry('900x600')
    t.mainloop()