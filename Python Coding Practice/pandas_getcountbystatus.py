#Get Count by Status using Pandas Dataframe APIs
# Example-1
import pandas as pd
data={'name': ['Customer A', 'Customer B', 'Customer C', 'Customer D', 'Customer E'],
    'id': [102, 101, 103, 104, 105],
    'usage': [450, 300, 600, 550, 400],
    'status': ['Active', 'Inactive', 'Active', 'Inactive', 'Active'],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B']
      }
df=pd.DataFrame(data)
print(df)
count_by_status=df.groupby('status').size()
print(count_by_status)

#Example-2
# BY passing null values
data= {
    'name': ['Customer A', 'Customer B', 'Customer C', 'Customer D', 'Customer E'],
    'id': [102, 101, 103, 104, 105],
    'usage': [450, 300, 600, 550, 400],
    'status': ['Active', None, 'Active', 'Inactive', 'Active']
}
df=pd.DataFrame(data)
print(df)
count_by_status=df.groupby("status").size()
print(count_by_status)
print('...................................................')
# Example-3
#Passing json data( use read_json)
json_data='''[
    {"name": "Customer A", "id": 102, "usage": 450, "status": "Active"},
    {"name": "Customer B", "id": 101, "usage": 300, "status": "Inactive"},
    {"name": "Customer C", "id": 103, "usage": 600, "status": "Active"},
    {"name": "Customer D", "id": 104, "usage": 550, "status": "Inactive"},
    {"name": "Customer E", "id": 105, "usage": 400, "status": "Active"}
]'''
print(json_data)
# To create data frame using json data
df=pd.read_json(json_data)
print(df)
print("Count by status:")
count_by_status=df.groupby("status").size()
print(count_by_status)
