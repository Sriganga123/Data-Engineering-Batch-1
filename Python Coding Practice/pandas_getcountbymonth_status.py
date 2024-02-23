#Get Count by Month and Status using Pandas Dataframe APIs
# Example-1
import pandas as pd

data={
    'name': ['Customer A', 'Customer B', 'Customer C', 'Customer D', 'Customer E','Customer F'],
    'id': [102, 101, 103, 104, 105,345],
    'usage': [450, 300, 600, 550, 400,890],
    'status': ['Active', 'Inactive', 'Active', 'Inactive', 'Active','Inactive'],
    'date': ['2024-01-15', '2024-02-20', '2024-01-05', '2024-02-10', '2024-02-25','2024-09-12']
}
df=pd.DataFrame(data)
#2.	Convert the relevant date column to a datetime type (if applicable).
df['date']=pd.to_datetime(df['date'])
#3.	Extract the month from the date column. and new column month is added
df['month']=df['date'].dt.month
#4.	Group the data by month and status columns.
count_by_status_month=df.groupby(['month','status']).size()
print(count_by_status_month)


# By passing json data
# Example-2
json_data= '''
[
    {"name": "Customer A", "id": 102, "usage": 450, "status": "Active", "date": "2024-01-15"},
    {"name": "Customer B", "id": 101, "usage": 300, "status": "Inactive", "date": "2024-02-20"},
    {"name": "Customer C", "id": 103, "usage": 600, "status": "Active", "date": "2024-01-05"},
    {"name": "Customer D", "id": 104, "usage": 550, "status": "Inactive", "date": "2024-02-10"},
    {"name": "Customer E", "id": 105, "usage": 400, "status": "Active", "date": "2024-02-25"}
]
'''
df=pd.read_json(json_data)
df["date"]=pd.to_datetime(df["date"])
df["month"]=df["date"].dt.month
print("Count by month and status:")
count_by_status_month=df.groupby(['month','status']).size()
print(count_by_status_month)

#Counting by Month and Status with Custom Date Format
# Example-3
data={
    'name': ['Customer A', 'Customer B', 'Customer C', 'Customer D', 'Customer E','Customer F'],
    'id': [102, 101, 103, 104, 105,890],
    'usage': [450, 300, 600, 550, 400,989],
    'status': ['Active', 'Inactive', 'Active', 'Inactive', 'Active','Inactive'],
    'date': ['15-Jan-2024', '20-Feb-2024', '05-Jan-2024', '10-Mar-2024', '25-Feb-2024','08-Jul-2022']
}
df=pd.DataFrame(data)
df["date"]=pd.to_datetime(df["date"],format="%d-%b-%Y")
df["month"]=df["date"].dt.month
print("Count by month and status")
count_by_status_month=df.groupby(["month","status"]).size()
print(count_by_status_month)
