import csv
file=open('Example-1.csv')
type(file)
rows = []
with open("Example-1.csv", 'r') as file:
   csvreader = csv.reader(file)
   header = next(csvreader)
   for row in csvreader:
       rows.append(row)
print(header)
print(rows)


#or
with open('Example-1.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[2:]
print(header)
print(rows)