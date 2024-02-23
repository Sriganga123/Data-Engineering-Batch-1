import json


def get_column_details(schema_file):

    with open(schema_file, "r") as f:
        schema = json.load(f)


    column_details = []
     for column in schema["columns"]:
        column_details.append({
        "name": column["name"],
        "type": column["type"],
        "description": column["description"],
    })


return column_details
schema_file = ".json"
column_details = get_column_details(schema_file)


for column in column_details:
    print(column["name"], column["type"], column["description"])