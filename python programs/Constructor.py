# Default constructor
class My_Class():
    def __init__(self):
        print("Default constructor")
        print('Hello')
obj1=My_Class()

# Parameterized Constructor
class My_Class:
    def __init__(self,a,b):
        print("Parameterized Constructor")
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
obj=My_Class(100,200)
