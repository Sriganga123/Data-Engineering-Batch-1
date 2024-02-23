# Unique elements from list
# 1) Using set method
def unique(list1):
    list_set=set(list1)
    unique_list=(list(list_set))
    for i in unique_list:
        print(i,end=' ')

# list1
list1=[1,3,2,1,2,67,22,44,33,33,22]
print('The unique elements in list1')
unique(list1)

# list2
list2=['a','b','c','d','b','c','e']
print('\nThe unique elements in list2')
unique(list2)
print('..............................')

# 2) Using reduce() function
from functools import reduce
def unique(list1):
    res=reduce(lambda re,x:re+[x] if x not in re else re ,list1,[])
    print(res)

# list1
list1=[12,54,8,12,9,3,8,9,3,8,10,1,3,2,2]
print('Unique elements in list1:')
unique(list1)
# list2
list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique values from 2nd list is")
unique(list2)
#print('..............................')

# 3) Using Operator.countOf() method
import operator as op
def unique(list1):
    unique_list=[]                              # initialize a null list
    for i in list1:                             # traverse for all elements
        if op.countOf(unique_list,i)==0:        # check if exists in unique_list or not
            unique_list.append(i)
    for i in unique_list:                       # print the list
        print(i,end=' ')

print('Unique elements:')
unique([1,2,2,4,4,4,5,5,9])
l1=['a','b','b','c','c','c']
print('\nUnique elements:')
unique(l1)
print('..........................')

# 4) using pandas module
import pandas as pd
def unique(list1):
    unique_list=pd.Series(list1).drop_duplicates().tolist()
    for i in unique_list:
        print(i,end=' ')
print('Unique elements using pandas:')
unique([1,2,2,4,4,4,5,5,9])
# list2
print('\nUnique elements using pandas in list-2')
list2=['a','a','b','b','c','c','Hello','Hello']
unique(list2)
print('\n.......................')

# 5) Using collections.Counter()
from collections import Counter
def unique(list1):
    print(*Counter(list1))

list1=[12,54,8,12,9,3,8,9,3,8,10,1,3,2,2]
print('Unique elements in list1:')
unique(list1)
# list2
list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]
print("\nthe unique elements in list2:")
unique(list2)
print('..............................')

# 6)Using dict.fromkeys()
list1=[10,10,20,30,40,70,30,40]
unique_list1=list(dict.fromkeys(list1))
print(unique_list1)
print('........................................')


#7)	Using map and set() method
my_list = [1, 2, 2, 3, 3, 4, 4, 5]
unique_elements = set(map(lambda x: x, my_list))
print(list(unique_elements))





