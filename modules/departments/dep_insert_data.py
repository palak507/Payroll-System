import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def dep_insert_scr():
    t = ttkb.Toplevel()
    t.title('DEPARTMENT - Insert')

    def savedata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b.get())
        xb = e.get()
        xc = g.get()
        sql = "insert into department values(%d,'%s','%s')" % (xa, xb, xc)
        cur.execute(sql)
        db.commit()
        b.delete(0, 100)
        e.delete(0, 100)
        g.delete(0, 100)
        db.close()
        messagebox.showinfo('Hi', 'Saved')

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="INSERT DATA", font=('Segoe UI', 20, 'bold'), bootstyle="primary").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Department ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    b.grid(row=1, column=1, pady=8)

    ttkb.Label(main_frame, text="Department Name", font=('Segoe UI', 11)).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 15))
    e = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    e.grid(row=2, column=1, pady=8)

    ttkb.Label(main_frame, text="HOD", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    g = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    g.grid(row=3, column=1, pady=8)

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.grid(row=4, column=0, columnspan=2, pady=(25, 0))
    ttkb.Button(btn_frame, text="Save", bootstyle="success", width=12, command=savedata).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=1, padx=5)

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")

    t.mainloop()