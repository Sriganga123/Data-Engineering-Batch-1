# create a empty set
s=set()
print(s)
# 1) add() method
# a) Add Element to an Empty set
s.add('s')
print(s)
s.add('o')
s.add('n')
s.add('a')
print(s)
# add 's' again
s.add('s')
print(s)
print('............')


# b) Add a new element to a Python set
s1={'s','o','n','a'}
# add m
s1.add('m')
print(s1)
# add 'm' again
s.add('m')
print(s1)
print('..................')

#c) Add element in a set that already exists
s2={1,4,66,8}
s2.add(66)
# since 66 is already present it gives same result
print(s2)
print('.........................')

# d) Adding any iterable to a set
s3={'s','o','n','a'}
t=(1,2,3)
l=['apple','mango','banana']
# adding a tuple
s3.add(t)
print(s3)
# adding list using update method
s3.update(l)
print(s3)
print('.....................')

# 2) clear
s={'sona',1,67,'Hello',78.90}
print(s)
s.clear()
print(s)
print('.....................')

# 3) copy()
# It creates a shallow copy of set
fruits={'apple','mango','banana','orange'}
fruit_copy=fruits.copy()
print('Copy of fruits:')
print(fruit_copy)
print('...............................................')

#Python program to demonstrate that copy created using set copy is shallow
first={'a','b','c','d'}
second=first.copy()
print(first)
print(second)

# add 'e' to second,original set first is not altered
second.add('z')
print(first)
print(second)
print('................................................')

# discard
first={'a','b','c','d'}
first.discard('c')
print(first)

# Discarding an element that is not present in set
first.discard('m')
print(first)