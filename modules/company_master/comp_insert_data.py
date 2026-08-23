import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def comp_insert_scr():
    t = ttkb.Toplevel()
    t.title('COMPANY MASTER - Insert')

    def savedata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b.get())
        xb = e.get()
        xc = g.get()
        xd = j.get()
        xe = m.get()
        xf = (p.get())
        sql = "insert into comp_master values(%d,'%s','%s','%s','%s','%s')" % (xa, xb, xc, xd, xe, xf)
        cur.execute(sql)
        db.commit()
        b.delete(0, 100)
        e.delete(0, 100)
        g.delete(0, 100)
        j.delete(0, 100)
        m.delete(0, 100)
        p.delete(0, 100)
        db.close()
        messagebox.showinfo('Hi', 'Saved')

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="INSERT DATA", font=('Segoe UI', 20, 'bold'), bootstyle="primary").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Company ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    b.grid(row=1, column=1, pady=8)

    ttkb.Label(main_frame, text="Name", font=('Segoe UI', 11)).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 15))
    e = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    e.grid(row=2, column=1, pady=8)

    ttkb.Label(main_frame, text="Address", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    g = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    g.grid(row=3, column=1, pady=8)

    ttkb.Label(main_frame, text="Email", font=('Segoe UI', 11)).grid(row=4, column=0, sticky=W, pady=8, padx=(0, 15))
    j = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    j.grid(row=4, column=1, pady=8)

    ttkb.Label(main_frame, text="Phone No", font=('Segoe UI', 11)).grid(row=5, column=0, sticky=W, pady=8, padx=(0, 15))
    m = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    m.grid(row=5, column=1, pady=8)

    ttkb.Label(main_frame, text="Registration No", font=('Segoe UI', 11)).grid(row=6, column=0, sticky=W, pady=8, padx=(0, 15))
    p = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    p.grid(row=6, column=1, pady=8)

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.grid(row=7, column=0, columnspan=2, pady=(25, 0))
    ttkb.Button(btn_frame, text="Save", bootstyle="success", width=12, command=savedata).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=1, padx=5)

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")

    t.mainloop()