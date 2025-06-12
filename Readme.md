# School Management System  
**By Gaurav Rayat**  

---

## 🎯 Why This Project?

Managing student and staff data in schools often requires expensive, proprietary software or APIs. This Python-based **School Management System** offers a free and efficient alternative. It allows administrators to register and manage student and staff records while providing analysis tools for Class 10 and 12 results.

> This is a command-line interface (CLI) application built in Python that helps schools manage essential administrative data. Admin users can be created using a secure *Secret Code*, known only to the head of the institution.  
> *(For demonstration, the secret code is included in the script as a comment.)*

---

## ✨ Features

- 🔒 Create new admin users (with secret code authentication)
- 👩‍🎓 Register new students (recent admissions)
- 👨‍🏫 Register new staff members
- 📋 View details of all students and staff
- 🔍 Search and display information of a particular student or staff member
- 🔢 View the total count of registered students and staff
- 📊 Analyze academic results for Classes 10 and 12
- ⚙️ Setup via `table.py` to initialize database tables

---

## ⚙️ Setup Instructions

1. Make sure you have **MySQL** installed and a **database already created**.
2. Run the `table.py` script to create the required tables.

### 🧩 `table.py` will:

- Prompt for your MySQL connection details
- Connect to the specified database
- Create the following tables:
  - `user` – stores admin user details
  - `student` – stores student information
  - `staff` – stores staff records

```bash
python table.py
```

3. Once tables are created, run the main program file to start using the system.

---

## 💡 Tech Stack

- **Python** (CLI-based app)
- **MySQL** (Backend database)
- `mysql-connector-python` (for database connection)

---

# Getting Started 🚀
***

## Clone the Repository
```bash
git clone https://github.com/GAURAV-RAYAT/school_management_system.git
cd school_management_system
```

## Install Requirements
Ensure you have Python 3 and pip installed. Then install the required libraries:
```bash
pip install -r requirements.txt
```

## Set Up the Database
Before running the application, make sure your MySQL database is set up.
Then run the `table.py` script to create required tables:
```bash
python table.py
```

## Start the Application
```bash
python main.py
```
