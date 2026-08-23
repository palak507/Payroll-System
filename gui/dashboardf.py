import tkinter
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from modules.company_master.comp_data_screen import *
from modules.company_master.comp_insert_data import *
from modules.company_master.comp_delete_data import *
from modules.company_master.comp_find_data import *
from modules.company_master.comp_update_data import *
from modules.company_master.comp_show_data import *
from modules.departments.dep_data_screen import *
from modules.departments.dep_delete_data import *
from modules.departments.dep_find_data import *
from modules.departments.dep_insert_data import *
from modules.departments.dep_show_data import *
from modules.departments.dep_update_data import *
from modules.employee_data.emp_data_screen import *
from modules.employee_data.emp_delete_data import *
from modules.employee_data.emp_find_data import *
from modules.employee_data.emp_insert_data import *
from modules.employee_data.emp_show_data import *
from modules.employee_data.emp_update_data import *
from modules.employee_salary_data.esal_data_screen import *
from modules.employee_salary_data.esal_delete_data import *
from modules.employee_salary_data.esal_find_data import *
from modules.employee_salary_data.esal_insert_data import *
from modules.employee_salary_data.esal_show_data import *
from modules.employee_salary_data.esal_update_data import *
from modules.employee_leave_data.leave_data_screen import *
from modules.employee_leave_data.leave_delete_data import *
from modules.employee_leave_data.leave_find_data import *
from modules.employee_leave_data.leave_insert_data import *
from modules.employee_leave_data.leave_show_data import *
from modules.employee_leave_data.leave_update_data import *
from modules.employee_loan_data.loan_data_screen import *
from modules.employee_loan_data.loan_delete_data import *
from modules.employee_loan_data.loan_find_data import *
from modules.employee_loan_data.loan_insert_data import *
from modules.employee_loan_data.loan_update_data import *
from modules.employee_loan_data.loan_show_data import *
from modules.salary_computation.salcom_data_screen import *
from modules.salary_computation.salcom_delete_data import *
from modules.salary_computation.salcom_find_data import *
from modules.salary_computation.salcom_insert_data import *
from modules.salary_computation.salcom_show_data import *
from modules.salary_computation.salcom_update_data import *
from modules.tax_computation.tax_data_screen import *
from modules.tax_computation.tax_delete_data import *
from modules.tax_computation.tax_find_data import *
from modules.tax_computation.tax_insert_data import *
from modules.tax_computation.tax_show_data import *
from modules.tax_computation.tax_update_data import *

def dashbrd(login_window=None):
    t = ttkb.Toplevel()
    t.title('COMPANY DASHBOARD')

    def cm():
        t.destroy()
        if login_window:
            login_window.deiconify()

    t.protocol("WM_DELETE_WINDOW", cm)

    header = ttkb.Frame(t, padding=20)
    header.pack(fill=X)
    ttkb.Label(header, text="COMPANY DASHBOARD", font=('Segoe UI', 24, 'bold'), bootstyle="info").pack(side=LEFT)
    ttkb.Button(header, text="LOGOUT", bootstyle="danger-outline", command=cm).pack(side=RIGHT)

    outer = ttkb.Frame(t)
    outer.pack(fill=BOTH, expand=True, padx=15, pady=10)

    from ttkbootstrap.style import Style
    theme_bg = Style().colors.bg

    canvas = Canvas(outer, highlightthickness=0, bg=theme_bg)
    scrollbar = ttkb.Scrollbar(outer, orient=VERTICAL, command=canvas.yview)
    scroll_frame = ttkb.Frame(canvas)

    canvas_window = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_canvas_configure(event):
        # Stretch the inner frame to match the canvas width so cards can expand to fill it
        canvas.itemconfig(canvas_window, width=event.width)

    scroll_frame.bind("<Configure>", on_frame_configure)
    canvas.bind("<Configure>", on_canvas_configure)

    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    modules = [
        ("Company Master", "primary", [
            ("Insert", comp_insert_scr), ("Update", comp_update_scr),
            ("Delete", comp_delete_scr), ("Find", comp_find_scr),
            ("View Data", comp_data_scr), ("Show All", comp_show_scr)]),
        ("Departments", "info", [
            ("Insert", dep_insert_scr), ("Update", dep_update_scr),
            ("Delete", dep_delete_scr), ("Find", dep_find_scr),
            ("View Data", dep_data_scr), ("Show All", dep_show_scr)]),
        ("Employees", "success", [
            ("Insert", emp_ins_scr), ("Update", emp_upd_scr),
            ("Delete", emp_del_scr), ("Find", emp_find_scr),
            ("View Data", emp_data_scr), ("Show All", emp_show_data)]),
        ("Employee Leaves", "warning", [
            ("Insert", leave_ins_scr), ("Update", leave_upd_scr),
            ("Delete", leave_del_scr), ("Find", leave_find_scr),
            ("View Data", leave_data_scr), ("Show All", leave_show_scr)]),
        ("Employee Loan", "info", [
            ("Insert", loan_ins_scr), ("Update", loan_upd_scr),
            ("Delete", loan_del_scr), ("Find", loan_find_scr),
            ("View Data", loan_data_scr), ("Show All", loan_show_scr)]),
        ("Employee Salary", "warning", [
            ("Insert", esal_ins_scr), ("Update", esal_upd_scr),
            ("Delete", esal_del_scr), ("Find", esal_find_scr),
            ("View Data", esal_data_scr), ("Show All", esal_show_scr)]),
        ("Salary Computation", "secondary", [
            ("Insert", salcom_ins_scr), ("Update", salcom_upd_scr),
            ("Delete", salcom_del_scr), ("Find", salcom_find_scr),
            ("View Data", salcom_data_scr), ("Show All", salcom_show_scr)]),
        ("Tax Computation", "danger", [
            ("Insert", tax_ins_scr), ("Update", tax_upd_scr),
            ("Delete", tax_del_scr), ("Find", tax_find_scr),
            ("View Data", tax_data_scr), ("Show All", tax_show_scr)]),
    ]

    cols = 4
    for c in range(cols):
        scroll_frame.grid_columnconfigure(c, weight=1)

    for idx, (title, color, buttons) in enumerate(modules):
        row, col = divmod(idx, cols)
        card = ttkb.Labelframe(scroll_frame, text=title, bootstyle=color, padding=15)
        card.grid(row=row, column=col, padx=12, pady=12, sticky="nsew")
        for b_text, b_cmd in buttons:
            ttkb.Button(card, text=b_text, bootstyle=f"{color}-outline", width=16, command=b_cmd).pack(pady=3, fill=X)

    # Auto-fit the window to the actual grid content, then center it on screen
    t.update_idletasks()
    content_width = scroll_frame.winfo_reqwidth() + scrollbar.winfo_reqwidth() + 40
    content_height = min(scroll_frame.winfo_reqheight() + 120, t.winfo_screenheight() - 100)

    screen_width = t.winfo_screenwidth()
    screen_height = t.winfo_screenheight()
    x = (screen_width - content_width) // 2
    y = (screen_height - content_height) // 2

    t.geometry(f"{content_width}x{content_height}+{x}+{y}")

    t.mainloop()