import tkinter as tk
from tkinter import ttk # Import the Treeview widget
from person import Person
from employee import Employee
from db_operations import DB_Operations

#person = Person("Kevin",23, "1234, andeson av, Ca")
# Creating an instances of the class 'Employee'

employee = Employee("Froylan", 25, "1234,Jose st, NY 70043", 54000, "GZ6014282", "EHS")

# Initialize the database operations
db = DB_Operations("employee_db.db")
root = tk.Tk()

def add_employee():
    print("new employee added")

def view_employees():
    # Add code to display employees in a GUI window
    # Create a Treeview widget for displaying employee
    tree = ttk.Treeview(root, columns=("Name", "Employee ID", "Department"))
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Employee ID")
    tree.heading("#3", text="Department")
    tree.grid(row=2, column=0, columnspan=2, padx=10, pady=10) # Place the Treeview below the buttons

    # Populate the Treeview with employee data
    #employee_window = tk.Top
    all_employees = db.get_all_employees()
    #root = tk.Tk()
    for employee in all_employees:
        name = employee['name']
        emp_id = employee['employee_id']
        department = employee['department']
        tree.insert("", "end", values=(name, emp_id, department))

    
    # Add code to open a GUI window for adding an employee
def create_gui():
    #root = tk.Tk()
    root.title("Employee Management GUI")
    # Add your gui elements here
    
    # Create labels
    label = tk.Label(root, text="Welcome to Employee Manager")
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


    # Create buttons
    view_button = tk.Button(root, text="View All Employees", command=view_employees)
    add_button = tk.Button(root, text="Add Employee", command=add_employee)

    # Pack buttons 
    view_button.grid(row=1, column=0, padx=10, pady=10)
    add_button.grid(row=1, column=1, padx=10, pady=10)

    root.mainloop()


def default_op():
   while True:
       print("\nEmployee Manager")
       print("1: View All Employee")
       print("2: Add Employee")
       print("3: Delete Employee")
       print("4: Update Salary")
       print("7: Exit")
       
       choice = input("Select from the menu: ")
       if choice == '1':
           all_employees = db.get_all_employees()
           print("    Names       -   Employee_ID  -  Department") 
           print('-------------------------------------------------')
           print('*************************************************')
           for employee in all_employees:
               print(employee['name'], ' - ',employee['employee_id'], ' - ', employee['department'])
               print('.................................................')

               # Close the database connection when done
            
       elif choice == '2':
           em_id = input ("Enter Employee ID: ")
           name = input("Enter Employee name: ")
           address = input("Enter Employee Address: ")
           age = input("Enter Employee age: ")
           salary = input("Enter Employee Salary: ")
           dept = input("Enter Employee Dept: ")
           my_employee = Employee(name, age,address,salary,em_id,dept)
           db.insert_employee(my_employee)

       elif choice == '3': 
           db.delete_employee(input("Enter Employee\'s ID who you want to delete"))
       elif choice == '4':
           db.update_employee(input("Enter of Emplyee ID who you want to update salary"),input("Enter New Salary Amount"))
       elif choice == '5': 
           print("Coming Soon")
       elif choice == '7': 
           break 
       else:
           print("Choice does not exist, Tree Again")

create_gui()
#default_op()
db.close_connection()
