# Sort python lists
# a) using sorted() function

l1=[89,23,11,1,-2,-1000]
print(l1)
# using sorted function
print('The sorted list is:')
print(sorted(l1))
print('..............................')

# b) sorted() function with reverse=True
print('The sorted list in descending order:')
print(sorted(l1,reverse=True))
print('.............................')

# c) sorted() function on strings
l2=['aa', 'BB', 'zz', 'CC']
print('Sorting strings:')
print(sorted(l2))

# Custom sorting with key
# 1) key=len
l3=['aaaa','bbbbbbbb','ccccccc','ddd','ee','f']
print("Sorting with len key")
print(sorted(l3,key=len))

# with reverse=True
print('Sorting with len key in descending order')
print(sorted(l3,key=len,reverse=True))


# 2)key=str.lower()
l4=['y','A','x','B','a','b','Y','X']
print('Sorting with str.lower() key')
print(sorted(l4,key=str.lower))


# 3) Creating our own key
# sorting based on last letter of string
def myFunc(s):
    return s[-1]

str=['ax','bd','Hello','Welcome','owl']
print('Creating own key')
print(sorted(str,key=myFunc))

# sorting based on age
def get_age(person):
    return person[1]
# list of tuples
l=[("Sona",22),("Mona",19),("Binnu",35),("Sunny",12)]
print(sorted(l,key=get_age))







# 4) itemgetter()
# (first name, last name, score) tuples
#itemgetter(1, 0) specifies that the sorting should be based on the second element(index=1 which is last name) first,
# and if there are ties, then by the first element(index=0 which is first name).
from operator import itemgetter
grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
print('Sorted using item getter')
print(sorted(grade, key=itemgetter(1,0)))
#itemgetter(0, -1) specifies that the sorting should be based on the first element (index=0 which is first name) first,
# and if there are ties, then by the last element (score) whose index is -1
print(sorted(grade, key=itemgetter(0, -1)))


# sort() method
l=[1,56,23,90,33,200,8989]
print('Using sort method')
l.sort()
print(l)
