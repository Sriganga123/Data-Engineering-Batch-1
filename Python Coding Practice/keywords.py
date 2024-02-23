# Keywords
# Print all the keywords in python
import keyword
print(keyword.kwlist)
print("The keywords in python are:")
count=0
for i in keyword.kwlist:
    print(i)
    count=count+1
print(f"Total number of keywords:{count}")