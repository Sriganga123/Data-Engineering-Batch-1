# default arguments
def fun(a,b=100):
    print(a,b)
fun(900)
fun(10,789)

#or
def details(name,age,salary=45000):
    print(f'Name:{name} Age:{age} Salary:{salary}')

details('Mona',19)