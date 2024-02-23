#operators
'''
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
#1) Arithmetic operators
print("Arithmetic operators")
a=15
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #Floor Division
print(a**b) #Exponentiation
print(a%b)

#2) Assignment operators
print("Assignment operators")
a=5
print(a)
a+=3
print(a)
a-=7
print(a)
a*=20
print(a)
a/=5
print(a)
a**=10
print(a)
a//=12
print(a)
a%=6
print(a)

# Comparison operators
print("Comparison operators")
a=12
b=17
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical operators
print("Logical operators")
x=30
print(x>5 and x<40)
print(x>20 or x<10 )
print(not(x>5) and x<30)

# Identity operators
print("Identity operators")
x=["A","B"]
y=["X","Y"]
z=x
print(x is z) #returns True because z is the same object as x
print(x is y) #returns False because x is not the same object as y, even if they have the same content

#Membership operator
print("Membership operators")
print("A" in x)
print("X" not in y)

#Bitwise operator
print("Bitwise operators")
a=12
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2) #Left shift multiply 2 times
print(a>>2) #Right shift divide 2 times