import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def comp_data_scr():
    t = ttkb.Toplevel()
    t.title('COMPANY MASTER - View Data')

    xa = []
    xb = []
    xd = []
    xe = []
    xf = []
    xg = []

    i = 0

    def filldata():
        db = get_connection()
        cur = db.cursor()
        sql = "select comp_id,name,address,email,phone_no,reg_no from comp_master"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            xa.append(res[0])
            xb.append(res[1])
            xd.append(res[2])
            xe.append(res[3])
            xf.append(res[4])
            xg.append(res[5])
        db.close()

    def firstrecord():
        nonlocal i
        i = 0
        _refresh()

    def nextrecord():
        nonlocal i
        i = i + 1
        _refresh()

    def prevrecord():
        nonlocal i
        i = i - 1
        _refresh()

    def lastrecord():
        nonlocal i
        i = len(xa) - 1
        _refresh()

    def _refresh():
        a1.delete(0, 100)
        b1.delete(0, 100)
        d1.delete(0, 100)
        e1.delete(0, 100)
        f1.delete(0, 100)
        g1.delete(0, 100)
        a1.insert(0, str(xa[i]))
        b1.insert(0, xb[i])
        d1.insert(0, xd[i])
        e1.insert(0, xe[i])
        f1.insert(0, xf[i])
        g1.insert(0, xg[i])

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="VIEW DATA", font=('Segoe UI', 20, 'bold'), bootstyle="primary").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Comp ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    a1 = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    a1.grid(row=1, column=1, pady=8)

    ttkb.Label(main_frame, text="Name", font=('Segoe UI', 11)).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 15))
    b1 = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    b1.grid(row=2, column=1, pady=8)

    ttkb.Label(main_frame, text="Address", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    d1 = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    d1.grid(row=3, column=1, pady=8)

    ttkb.Label(main_frame, text="Email", font=('Segoe UI', 11)).grid(row=4, column=0, sticky=W, pady=8, padx=(0, 15))
    e1 = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    e1.grid(row=4, column=1, pady=8)

    ttkb.Label(main_frame, text="Phone No", font=('Segoe UI', 11)).grid(row=5, column=0, sticky=W, pady=8, padx=(0, 15))
    f1 = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    f1.grid(row=5, column=1, pady=8)

    ttkb.Label(main_frame, text="Reg No", font=('Segoe UI', 11)).grid(row=6, column=0, sticky=W, pady=8, padx=(0, 15))
    g1 = ttkb.Entry(main_frame, width=30, bootstyle="primary")
    g1.grid(row=6, column=1, pady=8)

    nav_frame = ttkb.Frame(main_frame)
    nav_frame.grid(row=7, column=0, columnspan=2, pady=(20, 5))
    ttkb.Button(nav_frame, text="First", bootstyle="info", width=10, command=firstrecord).grid(row=0, column=0, padx=4)
    ttkb.Button(nav_frame, text="Previous", bootstyle="info", width=10, command=prevrecord).grid(row=0, column=1, padx=4)
    ttkb.Button(nav_frame, text="Next", bootstyle="info", width=10, command=nextrecord).grid(row=0, column=2, padx=4)
    ttkb.Button(nav_frame, text="Last", bootstyle="info", width=10, command=lastrecord).grid(row=0, column=3, padx=4)

    ttkb.Button(main_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=8, column=0, columnspan=2, pady=(20, 0))

    filldata()
    if xa:
        firstrecord()

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")

    t.mainloop()