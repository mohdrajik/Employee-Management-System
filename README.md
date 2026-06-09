# Employee Management System

A web-based Employee Management System built using Python, Flask, and MySQL. This application allows users to manage employee records through a simple and user-friendly interface.

## Features

* Add new employees
* View employee records
* Delete employee records
* MySQL database integration
* Responsive and clean user interface
* CRUD operations using Flask

## Technologies Used

* Python
* Flask
* MySQL
* HTML
* CSS

## Project Structure

```text
Employee-management-system/
│
├── app.py
├── templates/
│   ├── index.html
│   └── add_employee.html
├── static/
│   └── style.css
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd Employee-management-system
```

3. Install dependencies

```bash
pip install flask flask-mysqldb
```

4. Create the MySQL database and table

```sql
CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2)
);
```

5. Update MySQL credentials in `app.py`

6. Run the application

```bash
python app.py
```

7. Open in browser

```text
http://127.0.0.1:5000
```

## Future Improvements

* Employee update functionality
* Authentication and login system
* Search and filter employees
* Dashboard analytics
* Bootstrap-based responsive UI

## Author

Razik Shaikh

