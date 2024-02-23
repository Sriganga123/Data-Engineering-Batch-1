# Reading CSV data using pandas
# 1) read_csv method
import pandas as pd
data=pd.read_csv("Example-1.csv")
print(data)
print(type(data))
print("Names:")
print(data.Name)
print("Salary")
print(data.Salary)
# displays first 5 rows
print(data.head())
print('........................')
# 2) read_table method
print("Read table method")
data=pd.read_table("Example-1.csv",delimiter=',')
print(data)
print(type(data))
print('.......................')
# 3) Using the csv module
import csv
with open("Example-1.csv") as csv_file:
    csv_reader=csv.reader(csv_file)
    df=pd.DataFrame([csv_reader])
print(df)
print(type(df))






# 4) Using different parameters in read_csv
df = pd.read_csv("Example-1.csv",
                 sep=',',        # Delimiter
                 header='infer', # Use first row as column names
                 index_col=None, # Do not use any column as index
                 dtype={'ID': int, 'Name': str, 'Age': int, 'Salary': int}, # Data types for each column
                 parse_dates=False)
print(df)