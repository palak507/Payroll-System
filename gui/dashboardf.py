import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
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
    lt=''
    es=''
    et=''
    st=''
    dt=''
    ls=''
    sc=''
    tc=''
    def cm():
        t.destroy()
        if login_window:
            login_window.deiconify()
    t=tkinter.Tk()
    t.protocol("WM_DELETE_WINDOW",cm)
    t.geometry('1500x1500')
    t.title('DASHBOARD')
    x=Canvas(t,height=1500,width=1500,bg='lightblue')
    x.place(x=1,y=1)
    
    at=Label(t,text='COMPANY DASHBOARD',font=('algerian',25),bg='lightblue')
    at.place(x=550,y=30)
    a=Label(t,text='Master-Company table',font=('Bradley Hand ITC',15,'bold'),bg='indianred1')
    a.place(x=15,y=100)
    a1=Button(t,text='TAP TO INSERT',bg='peachpuff',command=comp_insert_scr)
    a1.place(x=75,y=150)
    a2=Button(t,text='TAP TO UPDATE',bg='salmon1',command=comp_update_scr)
    a2.place(x=70,y=200)
    a3=Button(t,text='TAP TO DELETE',bg='peachpuff',command=comp_delete_scr)
    a3.place(x=70,y=250)
    a4=Button(t,text='TAP TO FIND',bg='salmon1',command=comp_find_scr)
    a4.place(x=80,y=300)
    a5=Button(t,text='TAP TO VIEW DATA',bg='peachpuff',command=comp_data_scr)
    a5.place(x=60,y=350)
    a6=Button(t,text='TAP TO SHOW ALL DATA',bg='salmon1',command=comp_show_scr)
    a6.place(x=50,y=400)
    b=Label(t,text='Departments',font=('Bradley Hand ITC',15,'bold'),bg='pink')
    b.place(x=240,y=100)
    b1=Button(t,text='TAP TO INSERT',bg='violetred1',command=dep_insert_scr)
    b1.place(x=245,y=150)
    b2=Button(t,text='TAP TO UPDATE',bg='pink',command=dep_update_scr)
    b2.place(x=240,y=200)
    b3=Button(t,text='TAP TO DELETE',bg='violetred1',command=dep_delete_scr)
    b3.place(x=240,y=250)
    b4=Button(t,text='TAP TO FIND',bg='pink',command=dep_find_scr)
    b4.place(x=250,y=300)
    b5=Button(t,text='TAP TO VIEW DATA',bg='violetred1',command=dep_data_scr)
    b5.place(x=230,y=350)
    b6=Button(t,text='TAP TO SHOW ALL DATA',bg='pink',command=dep_show_scr)
    b6.place(x=210,y=400)
    d=Label(t,text='Employees',font=('Bradley Hand ITC',15,'bold'),bg='lightgreen')
    d.place(x=370,y=100)
    d1=Button(t,text='TAP TO INSERT',bg='forestgreen',command=emp_ins_scr)
    d1.place(x=375,y=150)
    d2=Button(t,text='TAP TO UPDATE',bg='lightgreen',command=emp_upd_scr)
    d2.place(x=370,y=200)
    d3=Button(t,text='TAP TO DELETE',bg='forestgreen',command=emp_del_scr)
    d3.place(x=370,y=250)
    d4=Button(t,text='TAP TO FIND',bg='lightgreen',command=emp_find_scr)
    d4.place(x=380,y=300)
    d5=Button(t,text='TAP TO VIEW DATA',bg='forestgreen',command=emp_data_scr)
    d5.place(x=360,y=350)
    d6=Button(t,text='TAP TO SHOW ALL DATA',bg='lightgreen',command=emp_show_data)
    d6.place(x=355,y=400)
    e=Label(t,text='Employee-Leaves',font=('Bradley Hand ITC',15,'bold'),bg='yellow')
    e.place(x=480,y=100)
    e1=Button(t,text='TAP TO INSERT',bg='gold2',command=leave_ins_scr)
    e1.place(x=515,y=150)
    e2=Button(t,text='TAP TO UPDATE',bg='yellow',command=leave_upd_scr)
    e2.place(x=510,y=200)
    e3=Button(t,text='TAP TO DELETE',bg='gold2',command=leave_del_scr)
    e3.place(x=510,y=250)
    e4=Button(t,text='TAP TO FIND',bg='yellow',command=leave_find_scr)
    e4.place(x=515,y=300)
    e5=Button(t,text='TAP TO VIEW DATA',bg='gold2',command=leave_data_scr)
    e5.place(x=500,y=350)
    e6=Button(t,text='TAP TO SHOW ALL DATA',bg='yellow',command=leave_show_scr)
    e6.place(x=500,y=400)
    f=Label(t,text='Employee-Loan',font=('Bradley Hand ITC',15,'bold'),bg='cyan2')
    f.place(x=650,y=100)
    f1=Button(t,text='TAP TO INSERT',bg='cyan4',command=loan_ins_scr)
    f1.place(x=675,y=150)
    f2=Button(t,text='TAP TO UPDATE',bg='cyan2',command=loan_upd_scr)
    f2.place(x=670,y=200)
    f3=Button(t,text='TAP TO DELETE',bg='cyan4',command=loan_del_scr)
    f3.place(x=670,y=250)
    f4=Button(t,text='TAP TO FIND',bg='cyan2',command=loan_find_scr)
    f4.place(x=675,y=300)
    f5=Button(t,text='TAP TO VIEW DATA',bg='cyan4',command=loan_data_scr)
    f5.place(x=665,y=350)
    f6=Button(t,text='TAP TO SHOW ALL DATA',bg='cyan2',command=loan_show_scr)
    f6.place(x=650,y=400)
    g=Label(t,text='Employee-Salary',font=('Bradley Hand ITC',15,'bold'),bg='darkorange')
    g.place(x=810,y=100)
    g1=Button(t,text='TAP TO INSERT',bg='orangered2',command=esal_ins_scr)
    g1.place(x=835,y=150)
    g2=Button(t,text='TAP TO UPDATE',bg='orange',command=esal_upd_scr)
    g2.place(x=830,y=200)
    g3=Button(t,text='TAP TO DELETE',bg='orangered2',command=esal_del_scr)
    g3.place(x=830,y=250)
    g4=Button(t,text='TAP TO FIND',bg='orange',command=esal_find_scr)
    g4.place(x=835,y=300)
    g5=Button(t,text='TAP TO VIEW DATA',bg='orangered2',command=esal_data_scr)
    g5.place(x=830,y=350)
    g6=Button(t,text='TAP TO SHOW ALL DATA',bg='orange',command=esal_show_scr)
    g6.place(x=815,y=400)
    h=Label(t,text='Salary Computation',font=('Bradley Hand ITC',15,'bold'),bg='mediumpurple1')
    h.place(x=985,y=100)
    h1=Button(t,text='TAP TO INSERT',bg='purple3',command=salcom_ins_scr)
    h1.place(x=1015,y=150)
    h2=Button(t,text='TAP TO UPDATE',bg='mediumpurple1',command=salcom_upd_scr)
    h2.place(x=1010,y=200)
    h3=Button(t,text='TAP TO DELETE',bg='purple3',command=salcom_del_scr)
    h3.place(x=1010,y=250)
    h4=Button(t,text='TAP TO FIND',bg='mediumpurple1',command=salcom_find_scr)
    h4.place(x=1015,y=300)
    h5=Button(t,text='TAP TO VIEW DATA',bg='purple3',command=salcom_data_scr)
    h5.place(x=1010,y=350)
    h6=Button(t,text='TAP TO SHOW ALL DATA',bg='mediumpurple1',command=salcom_show_scr)
    h6.place(x=995,y=400)
    j=Label(t,text='Tax Computation',font=('Bradley Hand ITC',15,'bold'),bg='red2')
    j.place(x=1190,y=100)
    j1=Button(t,text='TAP TO INSERT',bg='tomato',command=tax_ins_scr)
    j1.place(x=1205,y=150)
    j2=Button(t,text='TAP TO UPDATE',bg='red2',command=tax_upd_scr)
    j2.place(x=1200,y=200)
    j3=Button(t,text='TAP TO DELETE',bg='tomato',command=tax_del_scr)
    j3.place(x=1200,y=250)
    j4=Button(t,text='TAP TO FIND',bg='red2',command=tax_find_scr)
    j4.place(x=1205,y=300)
    j5=Button(t,text='TAP TO VIEW DATA',bg='tomato',command=tax_data_scr)
    j5.place(x=1200,y=350)
    j6=Button(t,text='TAP TO SHOW ALL DATA',bg='red2',command=tax_show_scr)
    j6.place(x=1185,y=400)
    ce=Button(t,text='CLICK TO EXIT',bg='black',fg='white',command=cm)
    ce.place(x=650,y=500)
    t.mainloop()