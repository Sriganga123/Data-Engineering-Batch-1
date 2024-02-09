
# Reading a file
fp=open('Datatypes.py','r')
print(fp.read())
fp.close()

# readLine() method
try:
    file=open('Functions.py','r')
    print(file.readline())
except Exception as e:
    print(e)
finally:
    file.close()

#readLines() method
try:
    file=open('Functions.py','r')
    print(file.readlines())
except Exception as e:
    print(e)
finally:
    file.close()

#write() method
text='Hello,Good Morning'
fp=open("xyz.txt",'w')
fp.write(text)
print('Done Writing')
fp.close()

# writeLines() method
fp=open('writelines.txt','w')
fp.writelines(["\nSee you soon!", "\nOver and out.","\nCome and join us"])
print("Done writing")
fp.close()

# append
try:
    file=open('app.txt','a')
    print(file.write('Hello Welcome'))
except Exception as e:
    print(e)
finally:
    file.close()

# seek() and tell()
fp=open('Datatypes.py','r')
fp.seek(67)
print(fp.tell())
print(fp.read())
fp.close()

#Copy the contents of one file into another
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
read('Datatypes.py','xyz.txt')
print("Contents copied successfully")