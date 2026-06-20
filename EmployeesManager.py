from utility import *
from Employee import *


class EmployeesManager:

    def __init__(self):
        self.employees = []

    def add_employee(self):

        print("\nEmployee Type")
        print("1. Manager")
        print("2. Developer")
        print("3. Intern")

        emp_type = input_is_valid("Choose type: ", 1, 3)

        name = input("Enter employee name: ")
        age = input_is_valid("Enter employee age: ")

        salary = input_is_valid("Enter salary/allowance: ")

        if emp_type == 1:
            emp = Manager(name, age, salary)

        elif emp_type == 2:
            emp = Developer(name, age, salary)

        else:
            emp = Intern(name, age, salary)

        self.employees.append(emp)

    def list_employee(self):

        if not self.employees:
            print("\nEmployee list is empty!")
            return

        for emp in self.employees:
            print(emp)

    def delete_employees_with_age(self, age_from, age_to):

        self.employees = [
            emp for emp in self.employees
            if not (age_from <= emp.age <= age_to)
        ]

    def find_employee_by_name(self, name):

        for emp in self.employees:
            if emp.name.lower() == name.lower():
                return emp

        return None

    def update_salary_by_name(self, name, salary):

        emp = self.find_employee_by_name(name)

        if emp is None:
            print("Employee not found")
            return

        print("Salary update not implemented for demo version.")