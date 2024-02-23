
#Parent table
class Bird:
    def __init__(self,name):
        self.name=name

    def print_info(self):
        print(f'This bird is:{self.name}')

    def fly(self):
        print('The bird can fly')

#child table-1
class Shalik(Bird):
    def __init__(self,name,color,character):
        #call the parent class method
        super().__init__(name)
        self.color=color
        self.character=character
    # override method
    def print_info(self):
        #call the method of parent class
        super().print_info()
        print(f'Color of bird:{self.color}')
        print(f'Character of bird:{self.character}')
    # override method
    def fly(self):
        print('It can fly high')


obj_Shalik=Shalik('Shalik','black','good')
obj_Shalik.print_info()
obj_Shalik.fly()