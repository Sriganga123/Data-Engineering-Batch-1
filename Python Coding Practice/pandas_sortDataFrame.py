import pandas as pd
employees=[(11, 'Jack',    44, 'Sydney',   19) ,
            (12, 'Riti',    41, 'Delhi' ,   17) ,
            (13, 'Aadi',    46, 'New York', 11) ,
            (14, 'Mohit',   45, 'Delhi' ,   15) ,
            (15, 'Veena',   43, 'Delhi' ,   14) ,
            (16, 'Shaunak', 42, 'Mumbai',   10 ),
            (17, 'Shaun',   40, 'Colombo',  12)]
df=pd.DataFrame(employees,columns=['ID','Name','Age','City','Experience'],index=['A','B','C','D','E','F','G'])
print(df)
#sort all rows in a data frame
print("Sort by experience")
df=df.sort_values(by=['Experience'])
print(df)
print("Sort by City:")
print(df.sort_values(by=['City']))
print("Sort by Age and City")
print(df.sort_values(by=['Age','City']))

# Sort by rows in descending order
print("Descending order")
print(df.sort_values(by=['Name'],ascending=False))


#Sort DataFrame by row index labels
print("Sort by Row Index")
print(df.sort_index())
#Sort DataFrame by column names
print("Sort DataFrame by column names")
print(df.sort_index(axis=1))