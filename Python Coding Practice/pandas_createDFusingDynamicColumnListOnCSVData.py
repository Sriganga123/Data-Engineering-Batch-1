import pandas as pd
# Read csv data into pandas dataframe
csv_data=pd.read_csv('UpdatedMarks.csv')
print(csv_data)
# Define dynamic column list
dynamic_list=['Name','English','Maths']
#Select the columns you want from the CSV data based on the dynamic column list
selected_data=csv_data[dynamic_list]
# Create a new DataFrame using the selected columns
df=pd.DataFrame(selected_data)
print(df)


# Example-2
data=pd.read_csv('Example-1.csv')
print(data)
dynamic_list=['ID','Name','Salary']
select_list=data[dynamic_list]
df1=pd.DataFrame(select_list)
print(df1)