from person import Person
class Employee(Person):

    def __init__(self,name,age,address,salary,employee_id,department):
        super().__init__(name,age,address)
        self._salary = salary
        self._employee_id = employee_id
        self._department = department


    def get_salary(self):
        return self._salary

    def set_salary(self,salary):
        self._salary = salary

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def get_department(self):
        return self._department

    def set_department(self,department):
        self._department = department
