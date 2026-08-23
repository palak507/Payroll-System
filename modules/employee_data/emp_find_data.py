import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def emp_find_scr():
    t = ttkb.Toplevel()
    t.title('EMPLOYEE DATA - Find')
    xt = []

    def filldata():
        db = get_connection()
        cur = db.cursor()
        sql = "select emp_id from emp_data order by emp_id"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()

    def finddata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b.get())
        sql = "select name,address,phone_no,doj,designation,dept_id from emp_data where emp_id=%d" % (xa)
        cur.execute(sql)
        data = cur.fetchone()
        f.delete(0, 100)
        h.delete(0, 100)
        m.delete(0, 100)
        p.delete(0, 100)
        u.delete(0, 100)
        r2.delete(0, 100)
        f.insert(0, data[0])
        h.insert(0, data[1])
        m.insert(0, data[2])
        p.insert(0, data[3])
        u.insert(0, data[4])
        r2.insert(0, str(data[5]))
        db.close()

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="FIND DATA", font=('Segoe UI', 20, 'bold'), bootstyle="info").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Emp ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b = ttkb.Combobox(main_frame, width=27, bootstyle="info")
    b.grid(row=1, column=1, pady=8)
    filldata()
    b['values'] = xt

    ttkb.Button(main_frame, text="Find", bootstyle="info", width=12, command=finddata).grid(row=2, column=0, columnspan=2, pady=10)

    ttkb.Label(main_frame, text="Name", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    f = ttkb.Entry(main_frame, width=30, bootstyle="info")
    f.grid(row=3, column=1, pady=8)

    ttkb.Label(main_frame, text="Address", font=('Segoe UI', 11)).grid(row=4, column=0, sticky=W, pady=8, padx=(0, 15))
    h = ttkb.Entry(main_frame, width=30, bootstyle="info")
    h.grid(row=4, column=1, pady=8)

    ttkb.Label(main_frame, text="Phone No.", font=('Segoe UI', 11)).grid(row=5, column=0, sticky=W, pady=8, padx=(0, 15))
    m = ttkb.Entry(main_frame, width=30, bootstyle="info")
    m.grid(row=5, column=1, pady=8)

    ttkb.Label(main_frame, text="DOJ", font=('Segoe UI', 11)).grid(row=6, column=0, sticky=W, pady=8, padx=(0, 15))
    p = ttkb.Entry(main_frame, width=30, bootstyle="info")
    p.grid(row=6, column=1, pady=8)

    ttkb.Label(main_frame, text="Designation", font=('Segoe UI', 11)).grid(row=7, column=0, sticky=W, pady=8, padx=(0, 15))
    u = ttkb.Entry(main_frame, width=30, bootstyle="info")
    u.grid(row=7, column=1, pady=8)

    ttkb.Label(main_frame, text="Dept ID", font=('Segoe UI', 11)).grid(row=8, column=0, sticky=W, pady=8, padx=(0, 15))
    r2 = ttkb.Entry(main_frame, width=30, bootstyle="info")
    r2.grid(row=8, column=1, pady=8)

    ttkb.Button(main_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=9, column=0, columnspan=2, pady=(25, 0))

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h_win = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h_win}+{(sw - w)//2}+{(sh - h_win)//2}")

    t.mainloop()