# Creating a class and obj
class My_Class:
    def __init__(self):
        self.x=0
        self.y=0
    def setData(self):
        self.x=1000
        self.y=2000
        self.z=3000
    def getData(self):
        print(f'Value of x {self.x} \nValue of y {self.y} \nValue of z {self.z}')
obj=My_Class()
obj.setData()
obj.getData()