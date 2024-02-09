#Public access modifier
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')

s=Student('Ashutosh',23)
s.display()


'''
# Private Access modifier
class BankAccount:
    def __init__(self,accno,balance):
        self.__accno=accno
        self.__balance=balance
    def __display(self):
        print(f'Account Number:{self.__accno}')
        print(f'Balance:{self.__balance}')

b=BankAccount(123345666,560000.90)
b.__display()
'''
# Protected Access Specifier
# Parent class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def _display(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
# Child class
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self._rollno=rollno
    def display(self):
        self._display()
        print(f'Rollno:{self._rollno}')

s=Student('Sona',22,78)
s.display()