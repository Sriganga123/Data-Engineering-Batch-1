'''Map in Python is a function that works as an iterator to return a result after applying a function
to every item of an iterable (tuple, lists, etc.).
It is used when you want to apply a single transformation function to all the iterable elements.'''

#map(function,iterables)
# 1) Square of a number using map
def square(i):
    return i*i
x=map(square,(2,3,4,5,6,7))
print(x)
print(list(x))

#or
num=(11,12,13,14,15)
result=map(square,num)
output=list(result)
print(output)

# 2) Using Map() With Len()
example=['Welcome','to','Python','Programming']
x=map(len,example)
print(f'Length of example:{list(x)}')