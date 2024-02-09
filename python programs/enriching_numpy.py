import numpy as np
'''
# List of values(Temperature in Celsius)
cvalues=[20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
C=np.array(cvalues)
# prints one dimensional numpy array
print(C)

# Convert C into Fareinheit
print("In Farenheit")
print(C*9/5+32)

# Value of C will not change
print("Value of C is same after manipulation")
print(C)

# type of C
print(type(C))
print('...............................')
# arange
a=np.arange(1,10)
print(a)

a=np.arange(10.4)
print(a)

a=np.arange(0.5,10.4,0.8)
print(a)

a=np.arange(2,89,7)
print(a)

# In this case stop value is also printed
a=np.arange(12.04, 12.84, 0.08)
print(a)

x = np.arange(0.5, 10.4, 0.8, int)
print(x)
print('..................................................')
# Examples on linspace
print("Linspace")

# by default takes num=50
print(np.linspace(1,5))

# num=5
print(np.linspace(9,15,5))

# by default endpoint is True
print(np.linspace(1,20,10))

# set endpoint=False
print(np.linspace(1,20,10,endpoint=False))
'''
#set retstep=True
print(np.linspace(1,20,10,retstep=True))

print(np.linspace(1,20,10,endpoint=False,retstep=True))

# To find only retstep value and sample separately
samples,spacing = np.linspace(1, 10, retstep=True)
print(samples)
print(spacing)
samples,spacing = np.linspace(1, 10, 20, endpoint=True, retstep=True)
print(samples)
print(spacing)
samples,spacing = np.linspace(1, 10, 20, endpoint=False, retstep=True)
print(samples)
print(spacing)
