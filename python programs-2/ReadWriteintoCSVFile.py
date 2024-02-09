
# Read CSV Files in python Using csv.reader
import csv
rows = []
with open("Example-1.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
print('.................................')

# read CSV Files Using .readlines()
with open('Example-1.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)

print('....................................................')

#Read CSV Files in python Using Pandas
import pandas as pd
#Load CSV files to pandas using read_csv()
data= pd.read_csv("Example-1.csv")
print(data)

# Extract the field names
print(data.columns)

# Extract rows
print(data.Age)
print(data.Salary)

print('....................................................')

# Read CSV file in python using csv.DictReader
# Open in mode 'r' for reading

with open('Example-1.csv','r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)

print('...............................................')


# Write CSV file Using csv.writer
# Records of 3 students
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
filename = 'Students_Data.csv.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data) # 5. write the rest of the data


# To check whether data is written or not
rows = []
with open("Students_Data.csv.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
# we can check in notepad as well
print('...................................')


# Write CSV File Using .writelines()
header = ['Name', 'Fname', 'Mname']
data = [['Sona', 'Raju', 'Dhana'], ['Chinnu','Satish','Madhavi'], ['Mona', 'Raju', 'Dhana']]
filename = 'Student_details.csv'
with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('\n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('\n')


# To check whether data is written or not using readlines()
with open('Student_details.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)


# Write CSV Using Pandas
# Create a pandas dataframe using pd.DataFrame
header = ['Name', 'Experience', 'Salary','age']
data = [['Alex', 6, 80000,45], ['Brad', 4, 56000,34], ['Joey', 5, 98000,47],['Ram',9,360000,54]]
data = pd.DataFrame(data, columns=header)
# Write to a CSV file using to_csv()
data.to_csv('Emp_data.csv', index=False)

# To check whether data is written or not using pandas
data=pd.read_csv('Emp_data.csv')
print(data)
print('...........................')


# Write CSV File Using csv.DictWriter
# Using the .open() function, create a new file object with the mode as ‘w’ for writing
with open('Family_Data.csv', 'w', newline='') as csvfile:
    data = [{'Name': 'Ram', 'Age': 12, 'Siblings': 2},
            {'Name': 'Latha', 'Age': 45, 'Siblings': 5},
            {'Name': 'Joy', 'Age': 85, 'Siblings': 4}]
    fieldnames = ['Name', 'Age', 'Siblings']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


# To check whether data is written or not
with open('Family_Data.csv','r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
