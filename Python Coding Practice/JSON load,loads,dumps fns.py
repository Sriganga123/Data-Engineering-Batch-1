#Convert JSON String to Dictionary Python
#json.loads(): to convert JSON string to a dictionary

# import json module
import json
# Define json string
jsonString='{"Name":"Sriganga","age":22,"Course":"Data Engineering"}'
# Convert JSON string into Python
student_details=json.loads(jsonString)
# Print Dictionary
print(student_details)
# To find type
print(type(student_details))
# Print values using keys
print(student_details['Name'])
print(student_details['age'])
print(student_details['Course'])


# Example-2
data='''{
            "Name":"Sriganga",
            "Contact":[6767676767,909099000],
            "Email":"sri@gmail.com",
            "Hobbies":["Reading","Listening Music"]
            }'''
res=json.loads(data)
print(res)
print(res['Contact'])
print('........................................')

#Convert JSON File to Python Object
# Example-1
with open('data.json') as json_file:
    data1=json.load(json_file)
print('Type:',type(data1))
print(data1)
print('Hobbies are:',data1['Hobbies'])
print('............................')

# Example-2
with open('data1.json') as json_file:
    data1=json.load(json_file)
print('Type:',type(data1))
print(data1)
print('Employees are:',data1['employees'])
print('....................................')


#Convert Nested JSON Object to Dictionary
# Example-1
with open('nested_json.json') as json_file:
    data1=json.load(json_file)
print(data1)
# for reading nested data- [0] represents the index value of the list
print(data1['isbn'][0])
print(data1['isbn'][1:8])
print(data1['editor']['lastname'])
print("isbn:", data1["isbn"])
print("Author Details:")
print("lastname:", data1["author"]["lastname"])
print("firstname:", data1["author"]["firstname"])
print("Editor Details:")
print("lastname:", data1["editor"]["lastname"])
print("firstname:", data1["editor"]["firstname"])
print("title:", data1["title"])
print("category:", data1["category"])
print('................................')

'''
# Example-2
with open('x.json') as json_file:
    data = json.load(json_file)
# for reading nested data [0] represents
# the index value of the list
    print(data['people1'][0])
# for printing the key-value pair of
# nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['people1']:
        print("Name:", i['name'])
        print("Website:", i['website'])
        print("From:", i['from'])
        print()
print('.............................................................')

'''
#Read, Write and Parse JSON using Python
#1)	Python read JSON file
f = open('emp.json', )
data1 = json.load(f)
print(data1)
for i in data1["emp_details"]:
    print(i)
f.close()
print('..............................')

#2) Convert Python Dict to JSON
dictionary = {
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
json_obj=json.dumps(dictionary,indent=4)
print("Dictionary is:")
print(json_obj)
print(type(json_obj))


#3) Writing JSON to a file in Python
dictionary={
    "t_name":"Dhana Laxmi",
    "t_id":200,
    "t_age":43,
    "t_salary":45000
}
with open("teacher.json","w") as outfile:
    json.dump(dictionary,outfile)
print("Teacher data dumped")
print('.............................................................')

#4)Python Pretty Print JSON
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
# Convert string to Python dict
employee_dict = json.loads(employee)
# Pretty Printing JSON string back
print(json.dumps(employee_dict, indent=4, sort_keys=True))
