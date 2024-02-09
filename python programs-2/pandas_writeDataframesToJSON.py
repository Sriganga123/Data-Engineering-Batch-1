import pandas as pd
# Example-1
data=[['a','b','c'],['d','e','f'],['g','h','i']]
df=pd.DataFrame(data,columns=['col1','col2','col3'],index=['row1','row2','row3'])
print(df)
print(type(df))
# converting to json
df.to_json('x.json',orient='split',compression='infer',index=True)
# Reading from that json file
df=pd.read_json('x.json')
print(df)
df=pd.read_json('x.json',orient='split')
print(df)
print('............................................................')

# Example-2
data=[['Sona',1,22,67,90,33,56],['Mona',2,19,89,44,66,89],['Sunny',3,23,56,77,88,99],['Bannu',4,27,55,99,33,89],
      ['Chinnu',5,24,78,90,56,45]]
df=pd.DataFrame(data,columns=['one','two','three','four','five','six','seven'],index=[1,2,3,4,5])
print(df)
print(type(df))
# writing to json file
df.to_json('stu.json',orient='split',compression='infer',index=True)
# reading from json file
df=pd.read_json('stu.json',orient='split')
print("JSON data")
print(df)