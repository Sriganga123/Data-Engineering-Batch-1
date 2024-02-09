# Example-1
l=[1,2,3,4]
a=2
try:
    x=10/2
    print(l[2])
    print(z)
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)


# User defined Exception
class Employee(Exception):
    def __init__(self,msg):
        super().__init__(msg)
name=input('Enter name:')
if name.replace(" ",'').isalpha():
    print('Name:',name)
else:
    try:
        raise Employee('Invalid name')
    except Employee as e:
        print(e)
salary=int(input("Enter Salary:"))
if salary<30000 or salary>100000:
    try:
        raise Employee('Invalid Salary')
    except Employee as e:
        print(e)
else:
    print('Salary:',salary)