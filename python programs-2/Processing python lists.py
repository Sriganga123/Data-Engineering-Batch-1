'''
list
====
1. index used
2. disimilar data
3. iterate with loop
4. duplicate allow
5. mutable
6. ordered
'''
print("List")
# Creating a list
l1=[10,20,30,40,50,10.5,10,20]
print(l1)

# Accessing elements of list
print(l1[6])
print(l1[1])

# Modifying elements
l1[6]=278
print(l1)
l2=[100,200,300]

# print all the functions of list
print(dir(l1))

# count of an element
print(l1.count(10))

# index of an elemnt
print(l1.index(40))

#function of list:
# add item in last
l1.append(45)
print(l1)

# remove an element
l1.remove(10.5)
print(l1)

#delete last element
l1.pop()
print(l1)

# Insert element
l1.insert(2,99)
print(l1)

#reverse the list
l1.reverse()
print(l1)

#sort the list
l1.sort(reverse=False)
print(l1)

#extend
l1.extend(l2)
print(l1)

# Iterate over loop
for i in l1:
    print(i,end=' ')

# List Comprehension
print('\n')
doubled = [x * 2 for x in l1]
print(doubled)

# Sorting a list
sorted_list = sorted(l1)
print(sorted_list)


#slicing
print("\nSlicing in list")
l2=[11,34.5,"Welcome",12,1,4,7,9,111,2222,989899]
print(l2)
print(l2[2:7])
print(l2[::]) # whole list
print(l2[::-1]) #reverse
print(l2[-5:-1])