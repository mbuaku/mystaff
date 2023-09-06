from person import Person
from employee import Employee
from db_operations import DB_Operations

#person = Person("Kevin",23, "1234, andeson av, Ca")
# Creating an instances of the class 'Employee'

employee = Employee("Froylan", 25, "1234,Jose st, NY 70043", 54000, "GZ6014282", "EHS")

# Initialize the database operations
db = DB_Operations("employee_db.db")

while True:
    print("\nEmployee Manager")
    print("1: View All Employee")
    print("2: Add Employee")
    print("3: Delete Employee")
    print("4: Update Salary")
    print("7: Exit")
    choice = input()

    if choice == '1':
        all_employees = db.get_all_employees()
        print("    Names       -   Employee_ID  -  Department")
        print('-------------------------------------------------')
        print('*************************************************')
        for employee in all_employees:
            print(employee['name'], ' - ',employee['employee_id'], ' - ', employee['department'])
            print('.................................................')
       
        # Close the database connection when done
       # db.close_connection()
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
    elif choice =='7':
        break
    else:
        print("Choice does not exist, Tree Again")

db.close_connection()
