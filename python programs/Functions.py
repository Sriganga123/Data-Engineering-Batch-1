# Functions
def greetings():
    print('Welcome to Python')
greetings()

def sum():
    print('Enter two numbers')
    a, b = map(int, input().split())
    return a+b
k=sum()
print(f'Sum={k}')

# or
def sum():
    print('Enter two numbers')
    a, b = map(int, input().split())
    c=a+b
    print(f'Sum={c}')
sum()

# a) Positional arguments
def fun(a,b):
    print(a,b)
fun(-10,10)
# b) default arguments
def fun(a,b=100):
    print(a,b)
fun(900)
fun(10,789)
#c) keyword arguments
def fun(a,b):
    print(a,b)
fun(a=234,b=789)
#d) variable length positional arguments
def fun(*args):
    print(type(args))
    for i in args:
        print(i,end=' ')
fun(10,20,30,40,50)

# or
def fun(*args):
    print(args[0],args[2])
fun(22,33,44,55,66)
#e) variable length keyword arguments
def fun(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,v,end=' ')
fun(name='Sona',rollno=12,marks=90)
# with argument with return type
# with argument without return type
# without argument with return type
# without argument without return type
#1)with argument with return type
def example(a,b):
    return a+b
print(example(2,7))
#2)with argument without return type
def example(a,b):
    print(f'Sum={a+b}')
example(2,7)
#3)without argument with return type
def example():
    return "Welcome,Good morning"
print(example())
#4)without argument without return type
def example():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(f'Sum={a+b}')
example()
#doc string
def foo():
    return 'Hiiiii'
print(foo())
help(foo)
