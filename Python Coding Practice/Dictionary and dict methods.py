#Dictionary
print("Dictionary")
student={101:'amit',102:'sumit',103:'somya',103:'somya','106':'Kartik'}
for i in student:
    print(i,student[i])
for i,j in student.items():
    print(i,j)
student[101]='Salman'
print(student)
student.update({105:'kiran'})
print(student)

d={101:'Amit',102:'Sumit',103:'Somya',104:'Sarthak',99:'SAMI',100:'sami'}
print(d.keys())
print(d.values())
print(d.items())
print(d.get(102))
d.pop(101)
print(d)
d.popitem()
print(d)

'''
d.keys()#return the all the keys
d.values()#return the all values
d.items()#return the key and value in pair
d.clear()#delete all key and values
d.get(101)#return the values
d.update({106:'Likitha'})#add the pair in the dict
d.pop(99)#delete the given key from the dict
d.popitem()#delete the last pair from dict
'''











    





