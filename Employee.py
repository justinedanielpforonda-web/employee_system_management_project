from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Age: {self.age}, Salary: {self.calculate_salary()}"


class Manager(Employee):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def calculate_salary(self):
        return self.__salary + 10000


class Developer(Employee):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def calculate_salary(self):
        return self.__salary + 5000


class Intern(Employee):

    def __init__(self, name, age, allowance):
        super().__init__(name, age)
        self.__allowance = allowance

    def calculate_salary(self):
        return self.__allowance