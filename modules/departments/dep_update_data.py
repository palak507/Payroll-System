import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def dep_update_scr():
    t = ttkb.Toplevel()
    t.title('DEPARTMENT DATA UPDATE')
    xt = []

    def filldata():
        db = get_connection()
        cur = db.cursor()
        sql = "select dept_id from department"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()

    def finddata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b.get())
        sql = "select dept_name,HOD from department where dept_id=%d" % (xa)
        cur.execute(sql)
        data = cur.fetchone()
        f.delete(0, 100)
        h.delete(0, 100)
        f.insert(0, data[0])
        h.insert(0, data[1])

    def update():
        db = get_connection()
        cur = db.cursor()
        xa = int(b.get())
        xb = f.get()
        xc = h.get()
        sql = "update department set dept_name='%s',HOD='%s' where dept_id=%d" % (xb, xc, xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi', 'Updated')
        b.delete(0, 100)
        f.delete(0, 100)
        h.delete(0, 100)
        db.close()

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="UPDATE DATA", font=('Segoe UI', 20, 'bold'), bootstyle="warning").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Dept ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b = ttkb.Combobox(main_frame, width=27, bootstyle="warning")
    b.grid(row=1, column=1, pady=8)
    filldata()
    b['values'] = xt

    ttkb.Button(main_frame, text="Find", bootstyle="info", width=12, command=finddata).grid(row=2, column=0, columnspan=2, pady=10)

    ttkb.Label(main_frame, text="New Dept Name", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    f = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    f.grid(row=3, column=1, pady=8)

    ttkb.Label(main_frame, text="New HOD", font=('Segoe UI', 11)).grid(row=4, column=0, sticky=W, pady=8, padx=(0, 15))
    h = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    h.grid(row=4, column=1, pady=8)

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.grid(row=5, column=0, columnspan=2, pady=(25, 0))
    ttkb.Button(btn_frame, text="Update", bootstyle="success", width=12, command=update).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=1, padx=5)

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h_win = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h_win}+{(sw - w)//2}+{(sh - h_win)//2}")

    t.mainloop()