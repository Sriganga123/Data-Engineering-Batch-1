#Nested loop
n=int(input("Enter a number:"))
for i in range(1,n):
    for j in range(1,n):
        print(i,j,end=' ')

#Multiplication table using nested loops
print('\n')
print("Multiplication tables from 1 to 5:")
for i in range(1,6):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}')
    print()