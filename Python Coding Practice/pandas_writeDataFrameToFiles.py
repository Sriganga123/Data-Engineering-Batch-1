import pandas as pd
# read excel data
d=pd.read_excel("Marks.xlsx")
df=pd.DataFrame(d)
print(df)
# Adding a column Total into Excel file
df['Total']=df['Telugu']+df['Hindi']+df['English']+df['Maths']
print(df)
# To export this modified file to excel
# New file UpdatedMarks.xlsx is created
#df.to_excel("UpdatedMarks1.xlsx",index=False)
# To remove index put index=False in above line

# Write to csv file
df.to_csv('UpdatedMarks.csv',index=False)
# reading from CSV file
print("Data from CSV file")
x=pd.read_csv("UpdatedMarks.csv")
print(x)

# Write to text file
print('Writing to txt file')
df.to_csv('UpdatedMarks.txt',sep=',',index=False)
print("Data from txt file")
x=pd.read_csv('UpdatedMarks.txt')
print(x)

# Write to html file
print('Writing to html file')
df.to_html('UpdatedMarks.html',index=False)
print("Data from HTML file")
y=pd.read_html('UpdatedMarks.html')
print(y)
