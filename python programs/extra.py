
#Data Members: instance,class variable
class My_Class:
    count=0        #class var
    def __init__(self,a,b): # instance var
        print("hi")
        self.a=a
        self.b=b
        print(self.a,self.b)
obj1=My_Class(299,499)
print(My_Class.count)
print(obj1.a)

class My_Class:
    def __init__(self,a,b):
        print("Parameterized Constructor")
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
    def __del__(self):
        print('Bye.... We are going to destroy')
obj=My_Class(100,200)
# static method
class MyClass:
    class_variable = "static"
    def __init__(self, a):
        self.a=100
        print(self.a)
    def static_method():                        # static method is called using class name
        print("This is a static method")
MyClass.static_method()












