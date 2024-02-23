#Square root using mapping function
import math
def sqrt(i):
    return math.sqrt(i)

res=map(sqrt,(16,256,1221,625))
print(res)
print(f'Square root:{list(res)}')

# Power of a number
power=[1,2,3,4]
base=[1,2,3,4]
result=list(map(pow,base,power))
print(f'Power of a number:{result}')