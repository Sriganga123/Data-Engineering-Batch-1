# Create a set
s={'g','e','k','s',12,100.2,'Hello','Welcome','t'}
print(s)
#1) add()
s.add('m')
print(f'Add:{s}')
#3) copy()
s1=s.copy()
print(f'Copy:{s1}')
#4) difference
s2={'apple','m','t',12,1222,908.111}
z=s.difference(s2)
print(f'Difference:{z}')
#5) difference_update()
#k=s2.difference_update(s)
#print(f'Difference update:{k}')
#print(s)
#6) discard
s.discard('Hello')
print(f'Discard:{s}')
#7) frozenset
print(f'Frozen Set:{frozenset(s)}')
#8) intersection
s3=s.intersection(s2)
print(f'Intersection:{s3}')
#9) intersection_update
#print(f'Intersection Update:{s.intersection_update(s2)}')
#print(s)
#10) pop()
print(f'Pop:{s.pop()}')
#11) remove
print(f'Remove:{s2.remove(908.111)}')
print(s2)
#12) symmetric diffrence
s4=s.symmetric_difference(s2)
print(f'Symmetric Difference:{s4}')
#13) symmetric_differnce_update
x=s.symmetric_difference_update(s2)
print(f'Symmetric Difference Update:{x}')
print(s)
#14) union
y=s.union(s2)
print(f'Union:{y}')
#15) Update
s7={'a',1,'b',2}
s.update(s7)
print(f'Update:{s}')
#16) issubset()
print(f'Subset:{s1.issubset(s2)}')
#17) issuperset()
print(f'Subset:{s1.issuperset(s2)}')

# Set methods
'''
1) add()--Adds a given element to a set
2) clear()--Removes all elements from the set
3) copy()--Returns a shallow copy of the set
4) difference()--Returns a set that is the difference between two sets(returns first set without common elements)
5) difference_update()--Updates the existing caller set with the difference between two sets(removes items existing in both sets)
6) discard()--Removes the element from the set
7) frozenset()--Return an immutable frozenset object
8) intersection()--Returns a set that has the intersection of all sets
9) intersection_update()--Updates the existing caller set with the intersection of sets
10) pop()--Returns and removes a random element from the set
11) remove()--Removes the element from the set
12) symmetric_difference()--returns a set that contains all items from both set, but not the items that are present in both sets.
13) symmetric_difference_update()--updates the original set by removing items that are present in both sets, and inserting the other items.
14) union()--Returns a set that has the union of all sets
15) update()--updates the current set, by adding items from another set
16) issubset()--Returns True if all elements of a set A are present in another set B
17) issuperset()--Returns True if all elements of a set A occupies set B



'''