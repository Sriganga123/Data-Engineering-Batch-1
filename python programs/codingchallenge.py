
#a)	Explain Pandas for Data Processing
import pandas as pd
# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
# Displaying the DataFrame
print("Original DataFrame:")
print(df)
# Sum
print("Sum of values grouped by name")
print(df.groupby('Name').sum())

# b)Execute Reading CSV Data using Pandas
import pandas as pd
#Load CSV files to pandas using read_csv()
data= pd.read_csv("Example-1.csv")
print(data)
print(type(data))
print("Print first five columns of data")
print(data.head())
print('...........................')

#c)	Read Data from CSV Files to Pandas Dataframes
# 1) read_csv method
import pandas as pd
data=pd.read_csv("Student_details.csv")
print(data)
print(type(data))
# display columns
print("Name")
print(data.Name)

 #2) using read_table() method
print("Read table method")
data=pd.read_table("Example-1.csv",delimiter=',')
print(data)
print(type(data))
print('...............................')

# 3) Using the csv module
import csv
with open("Example-1.csv") as csv_file:
    csv_reader=csv.reader(csv_file)
    df=pd.DataFrame([csv_reader])
print(df)
print(type(df))
print('..........................................')

#d) Filter Data in Pandas Dataframe using query.
data=pd.read_csv("Example-1.csv")
print(type(data))
a=data.query("Age==14")
print(a)
a=data.query('Name=="Sona"')
print(a)
print(data.query('Age>15'))

# Filter using multiple conditions
a=data.query('ID==4' and 'Age==23')
print(a)

a=data.query('ID==6' and 'Name==raju' and 'Salary==78000')
print(a)
print('...................................')


# 2)
#a)	Lambda functions in Python
#Sum of two numbers
print("Lambda function to find sum of two numbers")
sum=lambda x,y:print(f'Sum={x+y}')
sum(89,56)
sum(90.78,23.78)

# Square of a number
print("Lambda function to find square of a number")
square=lambda x:print(f'Square:{x*x}')
square(4)
square(29)

#b)Read JSON Strings to Python dicts or lists
import json
print("JSON Strings to Python Dictionary")
data='''{
            "Name":"Shivathmika",
            "Contact":[8787865558,1234567890],
            "Email":"shiva@gmail.com",
            "Hobbies":["Reading","Listening Music"],
            "Salary":670000,
            "Siblings":1
            }'''
res=json.loads(data)
print(res)
print(type(res))
print("Contact Details:",res['Contact'])
print("Salary:",res['Salary'])