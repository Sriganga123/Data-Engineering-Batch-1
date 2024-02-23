#Joins between Pandas dataframes
# create two dataframes a and b
import pandas as pd
a=pd.DataFrame()
print(a)
# Create dictionary
d={'id':[1,2,10,12],
   'val1':['a','b','c','d']}
a=pd.DataFrame(d)
print(a)

b=pd.DataFrame()
print(b)
d={'id':[1,2,9,8],
   'val1':['p','q','r','s']}
b=pd.DataFrame(d)
print(b)

# Inner join
print("Inner Join")
df=pd.merge(a,b,on='id',how='inner')
print(df)

# Left outer join
print("Left Outer Join")
df=pd.merge(a,b,on='id',how='left')
print(df)

# Right outer join
print("Right Outer Join")
df=pd.merge(a,b,on='id',how='right')
print(df)

# Full outer join
print("Full outer join")
df = pd.merge(a, b, on='id', how='outer')
print(df)

# Index Join
print("Index Join")
df=pd.merge(a,b,left_index=True,right_index=True)
print(df)
