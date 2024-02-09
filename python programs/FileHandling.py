# Reading a file
fp=open('Datatypes.py','r')
print(fp.read())
fp.close()

# Read first 10 characters
fp=open('Datatypes.py','r')
print(fp.read(10))
fp.close()

# Writing to file
text='Hello,Good Morning'
fp=open("typing.txt",'w')
fp.write(text)
print('Done Writing')
fp.close()
print('..............................')


# seek() and tell()
fp=open('Datatypes.py','r')
fp.seek(67)
print(fp.tell())
print(fp.read())
fp.close()

# append
try:
    file=open('typing.txt','a')
    print(file.write('Hello Welcome'))
except Exception as e:
    print(e)
finally:
    file.close()

# ReadLine()
try:
    file=open('Functions.py','r')
    print(file.readline())
except Exception as e:
    print(e)
finally:
    file.close()


# ReadLines
try:
    file=open('Functions.py','r')
    print(file.readlines())
except Exception as e:
    print(e)
finally:
    file.close()

# Copy contents
def read(f1,f2):
    try:
        file=open(f1,'r')
        txt=file.read()
        file=open(f2,'w')
        file.write(txt)
    except Exception as e:
        print(e)
    finally:
        file.close()
read('Datatypes.py','abc.txt')