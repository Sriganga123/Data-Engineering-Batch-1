# 1) sorting in descending order
import json
data='''{   
   "Student":[   
      {   
         "enrollment_no":"9915103000", 
         "name":"JIIT", 
         "subject":[   
            {   
               "code":"DBMS", 
               "grade":"C" 
            } 
         ] 
      }, 
      {   
         "enrollment_no":"8815103057", 
         "name":"JSS", 
         "subject":[   
            {   
               "code":"COA", 
               "grade":"A" 
            }, 
            {   
               "code":"CN", 
               "grade":"A+" 
            } 
         ] 
      } 
   ] 
}'''
# Parse JSON object
json_parse=json.loads(data)
print(json_parse)
print(data)

for i in json_parse["Student"]:
    print(i["enrollment_no"],i["name"],i["subject"])

for i in json_parse["Student"]:
    for j in i["subject"]:
        print(j['code'],j['grade'])

# Iterating
#sort the JSON first by code, then by grade and then by enrollment_no
for it in json_parse['Student']:
    for y in it['subject']:
        print(y['code'],y['grade'],it['enrollment_no'],it['name'])

print(".................................................................................................")

# 2) using json.dumps()
data={
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(data)
print(data["children"])
print(data["cars"])
for i in data['cars']:
    print(i["model"],i["mpg"])


print("Sort the result alphabetically by keys")
print(json.dumps(data,indent=4,sort_keys=True))
print(".........................................................")

#3) using sorted() function
json_data = '''
[
    {"name": "Customer A", "id": 102, "usage": 450},
    {"name": "Customer B", "id": 101, "usage": 300},
    {"name": "Customer C", "id": 103, "usage": 600}
]
'''
data = json.loads(json_data)
sorted_data = sorted(data, key=lambda x: x['id'])
print(data)
for i in data:
    print(i["name"],i["id"],i["usage"])
print("Sorted data based on key id is:")
print(sorted_data)
print('..................................................')

# 4) sorting by multiple fields
json_data = '''
[
    {"plan": "Plan A", "data_limit": 50, "price": 20},
    {"plan": "Plan B", "data_limit": 75, "price": 25},
    {"plan": "Plan C", "data_limit": 50, "price": 15}
]
'''
plans = json.loads(json_data)
for i in plans:
    print(i["plan"],i["data_limit"],i["price"])
def compare_plans(plan):
    return plan['data_limit'], plan['price']
sorted_plans = sorted(plans, key=compare_plans)
print(sorted_plans)
