# String functions
s='pythonprogramming'
print(type(s))
print(s[3])
print(dir(s))
l=[]
for i in dir(s):
    if i.startswith('__'):
        pass
    else:
        l.append(i)
print(l)

print(s[::])
print(s[::-1])
print(s[-5:-2])
print(s.upper())
print(s.lower())
print(s.strip())
print(s.capitalize())
print(s.title())
print(s.isalpha()) # if spaces are present it returns false
string='12345'
print(string.isdigit())
print(s.startswith('p'))
print(s.endswith('g'))
print(s.replace('p','P'))
print(s.find('i')) # returns index of first occurence
print(max(s)) # returns char with high value
print(min(s))
print(s.split('n'))
l=['D','e','l','h','i']
print(''.join(l))

# sorting a string
print(''.join(sorted(s)))
# reverse of string
print(s[::-1])
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')
str=''
for i in s:
    str=i+str
print(str)

