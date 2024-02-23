
#Module
import Calculator
Calculator.add(5,8)
print(Calculator.x)


# Renaming the module
import Calculator as cal
cal.mul(2,90)

from Calculator import mul,pow
mul(80,10)
pow(2,3)

from Calculator import *  # we can use any function since using *
div(10,2)

from math import sqrt,factorial
print(sqrt(256))
print(factorial(20))

from math import *
print(abs(-90))

#Import sys
import sys
print(sys.path)

