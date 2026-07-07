# Payroll and Resource System (PRS)

A desktop-based Payroll and Resource Management System built with Python (Tkinter) and MySQL, designed to manage company, department, employee, salary, leave, loan, and tax records through a simple GUI.

## Features

- **Admin Authentication**
  - Secure login for existing admins with credential verification against the database
  - Self-service signup screen for new admins to register their own accounts, with email OTP verification for added security
- Company master data management
- Department management
- Employee master data management
- Employee salary, leave, and loan tracking
- Salary computation and tax computation modules
- Full CRUD operations (Insert, Update, Delete, Find, View All) for every module
- Scrollable data views for large datasets

## Tech Stack

- **Language:** Python 3
- **GUI:** Tkinter, ttkbootstrap
- **Database:** MySQL (via PyMySQL)
- **Environment Management:** python-dotenv

## Project Structure

```
PRS/
├── main.py                      # Entry point — launches the login window
├── gui/
│   ├── login.py                 # Admin login screen
│   ├── signup.py                # New admin signup screen
│   └── dashboard.py             # Main dashboard — opens after login
├── modules/
│   ├── company_master/          # Company CRUD operations
│   ├── department/               # Department CRUD operations
│   ├── employee/                 # Employee CRUD operations
│   ├── employee_salary/          # Salary data CRUD operations
│   ├── employee_leave/           # Leave data CRUD operations
│   ├── employee_loan/            # Loan data CRUD operations
│   ├── salary_computation/       # Salary computation module
│   └── tax_computation/          # Tax computation module
├── database/
│   └── mysql_connector.py        # Centralized MySQL connection handler
├── .env                          # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/palak507/PRS.git
cd PRS
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root with the following:
```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=prs
```

### 5. Set up the database
Run the SQL scripts in `SQL REFERENCE.txt` (or your schema file) in MySQL to create the required tables:
- `comp_master`
- `department`
- `emp_data`
- `emp_salary_data`
- `emp_leave_data`
- `emp_loan_data`
- `salary_computation`
- `tax_computation`
- `admins`

### 6. Run the application
```bash
python main.py
```

## Database Schema Overview

| Table | Primary Key | References |
|---|---|---|
| `comp_master` | `comp_id` | — |
| `department` | `dept_id` | — |
| `emp_data` | `emp_id` | `dept_id` → `department` |
| `emp_salary_data` | — | `emp_id` → `emp_data` |
| `emp_leave_data` | — | `emp_id` → `emp_data` |
| `emp_loan_data` | — | `emp_id` → `emp_data`, `dept_id` → `department` |
| `salary_computation` | — | `emp_id` → `emp_data`, `dept_id` → `department` |
| `tax_computation` | — | `emp_id` → `emp_data`, `dept_id` → `department` |
| `admins` | `username` | — |

## Screenshots

*(Add screenshots of the login page, dashboard, and a data view here)*

## Author

**Palak Arora**
BTech CSE, BIET Agra
[Portfolio](https://palak507.github.io/Palak-Arora-Portfolio/) · [GitHub](https://github.com/palak507)

## License

This project is open source and available for educational purposes.