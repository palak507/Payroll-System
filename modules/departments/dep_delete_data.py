import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def dep_delete_scr():
    t = ttkb.Toplevel()
    t.title('DEPARTMENT - Delete')
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

    def deletedata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b.get())
        sql = "delete from department where dept_id=%d" % (xa)
        cur.execute(sql)
        b.delete(0, 100)
        messagebox.showinfo('Hi', 'Deleted')
        db.commit()
        db.close()

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="DELETE DATA", font=('Segoe UI', 20, 'bold'), bootstyle="danger").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Dept ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b = ttkb.Combobox(main_frame, width=27, bootstyle="danger")
    b.grid(row=1, column=1, pady=8)
    filldata()
    b['values'] = xt

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.grid(row=2, column=0, columnspan=2, pady=(25, 0))
    ttkb.Button(btn_frame, text="Delete", bootstyle="danger", width=12, command=deletedata).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="secondary", width=12, command=cm).grid(row=0, column=1, padx=5)

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")

    t.mainloop()