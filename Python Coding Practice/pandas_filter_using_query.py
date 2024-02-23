import pandas as pd
data=pd.read_csv("Example-1.csv")
print(type(data))
# replacing blank spaces with '_' ( only if necessary)
data.columns =[column.replace(" ", "_") for column in data.columns]
a=data.query("Age==14")
print(a)
a=data.query('Name=="Sona"')
print(a)
print(data.query('Age>15'))
print('..........................................')
# Filter using multiple conditions
a=data.query('ID==4' and 'Age==23')
print(a)

a=data.query('ID==6' and 'Name==raju' and 'Salary==78000')
print(a)

# More examples
#Records with salary>25000
print("Records with salary>25000")
salary_limit=25000
print(data.query('Salary>@salary_limit'))