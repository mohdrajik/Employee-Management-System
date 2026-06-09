from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Razikshaikh@098'
app.config['MYSQL_DB'] = 'employee_db'
mysql = MySQL (app)
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', employees=data)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        salary = request.form['salary']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO employees(name,email,department,salary) VALUES(%s,%s,%s,%s)",
            (name, email, department, salary)
        )
        mysql.connection.commit()
        cur.close()

        return redirect('/')

    return render_template('add_employee.html')

@app.route('/delete/<int:id>')
def delete_employee(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)