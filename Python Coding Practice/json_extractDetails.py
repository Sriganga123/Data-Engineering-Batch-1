import json
# Example-1
json_data = '[{"id": 1, "name": "John", "age": 30}, {"id": 2, "name": "Alice", "age": 25}]'
x=json.loads(json_data)
print(x)
print(type(x))
print(x[0])
for i in x:
    print(i["name"])
    print(i["age"])

# Filtering and extracting specific details
filtered_data=[i for i in x if i['age']>25]
for i in filtered_data:
    print(i['name'],i['age'])
print("....................")



# Example-2
json_data = '[{"id": 1, "name": "John", "addresses": [{"city": "New York", "zip": "10001"}, {"city": "Los Angeles", "zip": "90001"}]}, {"id": 2, "name": "Alice", "addresses": [{"city": "Chicago", "zip": "60601"}, {"city": "Houston", "zip": "77001"}]}]'
x=json.loads(json_data)
print(type(x))
print(x[0])
print(x[1])
for i in x:
    print(i["id"])
    print(i["addresses"][0])
print('............................')
for i in x:
    for j in i["addresses"]:
        print(j["city"],j["zip"])


