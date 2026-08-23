import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def loan_ins_scr():
    t = ttkb.Toplevel()
    t.title('EMPLOYEE LOAN - Insert')

    def savedata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b1.get())
        xb = int(d1.get())
        xc = int(g1.get())
        sql = "insert into emp_loan_data values(%d,%d,%d)" % (xa, xb, xc)
        cur.execute(sql)
        db.commit()
        b1.delete(0, 100)
        d1.delete(0, 100)
        g1.delete(0, 100)
        db.close()
        messagebox.showinfo('Hi', 'Saved')

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="INSERT DATA", font=('Segoe UI', 20, 'bold'), bootstyle="info").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Emp ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b1 = ttkb.Entry(main_frame, width=30, bootstyle="info")
    b1.grid(row=1, column=1, pady=8)

    ttkb.Label(main_frame, text="Dept ID", font=('Segoe UI', 11)).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 15))
    d1 = ttkb.Entry(main_frame, width=30, bootstyle="info")
    d1.grid(row=2, column=1, pady=8)

    ttkb.Label(main_frame, text="Loan Amount", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    g1 = ttkb.Entry(main_frame, width=30, bootstyle="info")
    g1.grid(row=3, column=1, pady=8)

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