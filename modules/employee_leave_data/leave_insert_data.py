import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def leave_ins_scr():
    t = ttkb.Toplevel()
    t.title('EMPLOYEE LEAVE - Insert')

    def savedata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b1.get())
        xb = (d1.get())
        xc = (g1.get())
        xd = (j1.get())
        sql = "insert into emp_leave_data values(%d,'%s','%s','%s')" % (xa, xb, xc, xd)
        cur.execute(sql)
        db.commit()
        b1.delete(0, 100)
        d1.delete(0, 100)
        g1.delete(0, 100)
        j1.delete(0, 100)
        db.close()
        messagebox.showinfo('hi', 'saved')

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="INSERT DATA", font=('Segoe UI', 20, 'bold'), bootstyle="warning").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Emp ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    b1.grid(row=1, column=1, pady=8)

    ttkb.Label(main_frame, text="Month", font=('Segoe UI', 11)).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 15))
    d1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    d1.grid(row=2, column=1, pady=8)

    ttkb.Label(main_frame, text="No. of Leaves", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    g1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    g1.grid(row=3, column=1, pady=8)

    ttkb.Label(main_frame, text="Type", font=('Segoe UI', 11)).grid(row=4, column=0, sticky=W, pady=8, padx=(0, 15))
    j1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    j1.grid(row=4, column=1, pady=8)

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.grid(row=5, column=0, columnspan=2, pady=(25, 0))
    ttkb.Button(btn_frame, text="Save", bootstyle="success", width=12, command=savedata).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=1, padx=5)

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h}+{(sw - w)//2}+{(sh - h)//2}")

    t.mainloop()