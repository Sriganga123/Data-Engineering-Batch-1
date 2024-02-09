#Variable length positional arguments

def fun(*args):
    print(type(args))
    for i in args:
        print(i,end=' ')
fun(10,20,30,40,50)

# or
# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (f'\nSum:{result}')

#Variable length keyword arguments

def address(**kwargs):
   for k,v in kwargs.items():
      print(f'{k}:{v}')
print('Variable length keyword arguments')
print ("pass four keyword args")
address(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")
