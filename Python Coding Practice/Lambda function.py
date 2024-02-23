'''A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression'''

#1) simple example
print('Simple example using lambda function')
greet=lambda:print("Hello,Welcome to Python")
greet()

#2) Lambda function with  arguments
print("Lambda function with args")
Details=lambda name,age:print(f'I am {name} and I am {age} years old')
Details('Sriganga',22)

#3) Sum of two numbers
print("Lambda function to find sum of two numbers")
sum=lambda x,y:print(f'Sum={x+y}')
sum(12,45)
sum(1.55,54.98)

