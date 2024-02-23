import json

import pandas as pd
# Reading json data
data = pd.read_json('jsondata.json')
print (data)
# To print first 5 rows
print(data.head())

#Reading Specific Columns and Rows
# use multi-axes indexing method (.loc())
print(data.loc[[1,3,5],['Name','Salary']])

#Reading JSON file as Records
#to_json function along with parameters to read the JSON file content into individual records.
print(data.to_json(orient='records',lines=True))

# Parsing json string
data='{"Name":"Sona","Age":22,"Hobbies":["Reading","Playing"],"salary":50000}'
print(type(data))
x=json.loads(data)
print(x)
print(x["Hobbies"])
print(type(x))

# parsing json data
# Convert json file to python obj
# convert python obj to JSON
# writing python obj to json file