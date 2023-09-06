import sqlite3

class DB_Operations:
    def __init__(self,db_file):
        # Initialize the database connection and cursor
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        # Create the employee table if it doesn't exist
        self.create_table()


    def create_table(self):
        # Create the 'employees' table with columns for employee information
        self.cursor.execute('''
           CREATE TABLE IF NOT EXISTS employees (
              id INTEGER PRIMARY KEY,
              name TEXT,
              age INTEGER,
              address TEXT,
              salary REAL,
              employee_id TEXT,
              department TEXT
            )
        ''')
        # Commit the table creation to the database
        self.conn.commit()


    def insert_employee(self, employee):
        # Insert a new employee record into the 'employees' table
        self.cursor.execute('''
           INSERT INTO employees (name, age, address, salary, employee_id, department)
           VALUES (?,?,?,?,?,?)
        ''', (employee.get_name(), employee.get_age(), employee.get_address(), employee.get_salary(), employee.get_employee_id(), employee.get_department()))
        # Commit the insertion to the database
        self.conn.commit()

    def update_employee(self, employee_id, new_salary):
        # Update an employee's salary based on their employee_id
        self.cursor.execute('''
           UPDATE employees
           SET salary = ?
           WHERE employee_id = ?
        ''', (new_salary, employee_id))
        # Commit the update to the database
        self.conn.commit()

    def get_all_employees(self):
        # Retrieve all employee records from the 'employees' table
        self.cursor.execute('SELECT * FROM employees')
        # Fetch all the records as a list of dictionaries
        rows = self.cursor.fetchall()

        # Define a list to store employee records as dictionaries
        employee_list = []
        for row in rows:
            # Create a dictionary for each employee record
            employee = {
                    'id' : row[0],
                    'name' : row[1],
                    'age' : row[2],
                    'address' : row[3],
                    'salary' : row[4],
                    'employee_id' : row[5],
                    'department' : row[6]
                }
            # Append the employee dictionary to the list
            employee_list.append(employee)

        return employee_list    

    def get_employee(self, employee_id):
        # Retrieve an employee's information based on their employee_id
        self.cursor.execute('''
           SELECT * FROM employees
           WHERE employee_id = ?
        ''', (employee_id,))
        # Return the first matching record as a tuple
        return self.cursor.fetchone()

    def delete_employee(self, employee_id):                                                    # Delete an employee record based on their employee_id
        self.cursor.execute('''
            DELETE FROM employees                                                                   WHERE employee_id = ?                                                                ''', (employee_id,))
        # Commit the deletion to the database
        self.conn.commit()

       
    def close_connection(self):
        # Close the database connection
        
        self.conn.close()

