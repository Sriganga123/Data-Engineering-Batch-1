
# Example of Lambda Function
str1 = 'welcome to python programming'

upper = lambda string: string.upper()
print(upper(str1))


# Usage of Lambda Function
#1) Condition Checking
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))

#2) Python Lambda Function with List Comprehension

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())


#3) Python Lambda Function with if-else

Max = lambda a, b : a if(a > b) else b
print(Max(12,89))

# Python Lambda with Multiple Statements to find second maximum number

List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)

# Using lambda() Function with filter()
# i) Filter out all odd numbers using filter() and lambda function

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# ii) Filter all people having age more than 18, using lambda and filter() function
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))

print(adults)

# Using lambda() Function with map()
# i) Multiply all elements of a list by 2 using lambda and map() function

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

# ii) Transform all elements of a list to upper case using lambda and map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: animal.upper(), animals))
print(uppered_animals)



# Using lambda() function with reduce
# i) A sum of all elements in a list using lambda and reduce() function
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)

#ii)Find the maximum element in a list using lambda and reduce() function
import functools
lis = [1, 3, 5, 6, 2 ]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# or
from functools import reduce
lis=[1,3,5,6,2]
max=reduce((lambda a,b:a if a>b else b),lis)
print(max)
