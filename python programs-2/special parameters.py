'''Python have the special forms of parameters in functions.
These special forms of parameters are Args and Kwargs.
Args is a special parameter through which any number of positive arguments packed into a tuple.
Through Kwargs any number of Keyword Arguments packed into a dictionary.
'''
# Args example
def fruits(*args):
    for i in args:
        print(i)

print("Fruits:")
fruits('apple','mango','banana','berry')

# Kargs example
def winner(**kwargs):
    for k,v in kwargs.items():
        print(f'Key:{k} Value:{v}')

winner(First='Sona',Second='Mona',Third='Dinnu')