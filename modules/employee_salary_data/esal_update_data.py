import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from database.mysql_connector import get_connection

def esal_upd_scr():
    t = ttkb.Toplevel()
    t.title('EMPLOYEE SALARY - Update')
    xt = []

    def filldata():
        db = get_connection()
        cur = db.cursor()
        sql = "select emp_id from emp_salary_data order by emp_id"
        cur.execute(sql)
        data = cur.fetchall()
        for res in data:
            xt.append(res[0])
        db.close()

    def finddata():
        db = get_connection()
        cur = db.cursor()
        xa = int(b1.get())
        sql = "select ctc,variable_pay,slab,grade from emp_salary_data where emp_id=%d" % (xa)
        cur.execute(sql)
        data = cur.fetchone()
        d1.delete(0, 100)
        g1.delete(0, 100)
        j1.delete(0, 100)
        e1.delete(0, 100)
        d1.insert(0, data[0])
        g1.insert(0, data[1])
        j1.insert(0, data[2])
        e1.insert(0, data[3])
        db.close()

    def update():
        db = get_connection()
        cur = db.cursor()
        xa = int(b1.get())
        xb = int(d1.get())
        xc = int(g1.get())
        xd = j1.get()
        xe = e1.get()
        sql = "update emp_salary_data set ctc=%d,variable_pay=%d,slab='%s',grade='%s' where emp_id=%d" % (xb, xc, xd, xe, xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Hi', 'Updated')
        d1.delete(0, 100)
        g1.delete(0, 100)
        j1.delete(0, 100)
        e1.delete(0, 100)
        db.close()

    def cm():
        t.destroy()

    main_frame = ttkb.Frame(t, padding=30)
    main_frame.pack(expand=True, fill=BOTH)

    ttkb.Label(main_frame, text="UPDATE DATA", font=('Segoe UI', 20, 'bold'), bootstyle="warning").grid(row=0, column=0, columnspan=2, pady=(0, 25))

    ttkb.Label(main_frame, text="Emp ID", font=('Segoe UI', 11)).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 15))
    b1 = ttkb.Combobox(main_frame, width=27, bootstyle="warning")
    b1.grid(row=1, column=1, pady=8)
    filldata()
    b1['values'] = xt

    ttkb.Button(main_frame, text="Find", bootstyle="info", width=12, command=finddata).grid(row=2, column=0, columnspan=2, pady=10)

    ttkb.Label(main_frame, text="CTC", font=('Segoe UI', 11)).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 15))
    d1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    d1.grid(row=3, column=1, pady=8)

    ttkb.Label(main_frame, text="Variable Pay", font=('Segoe UI', 11)).grid(row=4, column=0, sticky=W, pady=8, padx=(0, 15))
    g1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    g1.grid(row=4, column=1, pady=8)

    ttkb.Label(main_frame, text="Slab", font=('Segoe UI', 11)).grid(row=5, column=0, sticky=W, pady=8, padx=(0, 15))
    j1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    j1.grid(row=5, column=1, pady=8)

    ttkb.Label(main_frame, text="Grade", font=('Segoe UI', 11)).grid(row=6, column=0, sticky=W, pady=8, padx=(0, 15))
    e1 = ttkb.Entry(main_frame, width=30, bootstyle="warning")
    e1.grid(row=6, column=1, pady=8)

    btn_frame = ttkb.Frame(main_frame)
    btn_frame.grid(row=7, column=0, columnspan=2, pady=(25, 0))
    ttkb.Button(btn_frame, text="Update", bootstyle="success", width=12, command=update).grid(row=0, column=0, padx=5)
    ttkb.Button(btn_frame, text="Close", bootstyle="danger", width=12, command=cm).grid(row=0, column=1, padx=5)

    t.update_idletasks()
    w = main_frame.winfo_reqwidth() + 60
    h_win = main_frame.winfo_reqheight() + 60
    sw, sh = t.winfo_screenwidth(), t.winfo_screenheight()
    t.geometry(f"{w}x{h_win}+{(sw - w)//2}+{(sh - h_win)//2}")

    t.mainloop()