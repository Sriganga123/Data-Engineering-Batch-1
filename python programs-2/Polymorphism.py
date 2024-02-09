#Polymorphism
class Person: # parent class
    def __init__(self):
        self.height=157
        self.weight=60
        self.comp='fair'
    def display(self):
        print(self.height,self.weight,self.comp)
class Student(Person) :# child class
    def __init__(self):
        self.name='Mona'
        self.course='BTech'
    def display(self):
        print(self.name,self.course)
obj=Student()
obj.display()       # overriding takes place and displays child class details


# TO print parent class details use super/calls the base class constructor
class Person: # parent class
    def __init__(self):
        self.height=157
        self.weight=60
        self.comp='fair'
    def display(self):
        print(self.height,self.weight,self.comp)
class Student(Person) :# child class
    def __init__(self):
        self.name='Mona'
        self.course='BTech'
        super().__init__()
    def display(self):
        print(self.name,self.course)
        super().display()
obj=Student()
obj.display()