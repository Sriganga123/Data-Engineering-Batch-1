import pandas as pd
# Create dataframe
data=[[9, 4, 8, 9],
      [8, 10, 7, 6],
      [7, 6, 8, 5]]
df=pd.DataFrame(data,columns=['Maths',  'English',
             'Science', 'History'])
print(df)

# 1) sum()
print("Sum")
Sum=df.sum()
print(Sum)

#2) min()
print("Minimum")
Min=df.min()
print(Min)

#3) max()
print("Maximum")
Max=df.max()
print(Max)

# 4) mean()
print("Mean")
Mean=df.mean()
print(Mean)
'''
#5) size
print("Size")
Size=df.size()  # int object is not callable
print(Size)
'''

# 6) describe
print('describe')
print(df.describe())
print("Agg function")
# 7) agg()
print(df.agg(['sum','min','max','mean','median','prod']))

# 8) group by
a=df.groupby("Maths")
print(a.first())

# group by multiple columns
# First group by Maths and later by english
a=df.groupby(['Maths','English'])
print(a.first())

print('........................................')

# creating an another dataframe
data=[["Sona",1,95, 42, 80, 92],
      ["Mona",8, 100, 72, 60,89],
      ["Chinnu",7, 67, 83, 52,77],
      ["Bannu",1,34,19,56,45],
      ["Sunny",7,33,66,77,76]]
df=pd.DataFrame(data,columns=['Name','ID','Maths','Physics','Chemistry','Biology'])
print(df)
# group by add and find sum
print(df.groupby('ID').sum())

'''
# group by two columns( first by ID and then by Name)
a=df.groupby(['ID','Name'])
print(a.first())

# group by two columns(First by Name and then ID)
a=df.groupby(['ID','Name'])
print(a.last())
'''
print(df.groupby('Name').mean())
print(df.groupby('ID').sum())
print(df.groupby('ID').min())
print(df.groupby('Name').min())
print(df.groupby(['ID']).max())
print(df.agg(['min','max','sum']))
print(df.groupby('Name').agg(['sum','min','max','mean']))













