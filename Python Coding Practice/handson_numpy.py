import numpy as np
# Version
print("Version")
print(np.__version__)
# 0 D array
print("0 D array")
a=np.array(67)
print(a)
print("Dimension")
# dimension
print(a.ndim)
print(type(a))
# 1 D array
print("1 D array")
a=np.array([1,45,66,33])
print(a)
print("Dimension")
# dimension
print(a.ndim)
print(type(a))
# 2 D array
print("2 D array")
a=np.array([[1,2,3],[6,7,9]])
print(a)
print("Dimension")
# dimension
print(a.ndim)
print(type(a))
# 3 D array
print("3 D array")
a=np.array([[[1,2,3,4],[8,6,4,6]],[[7,3,3,3],[22,44,3,22]]])
print(a)
print("Dimension")
# dimension
print(a.ndim)
print(type(a))
# Access array elements
print("Access Array elements")
a=np.array([21,55,33,77,89])
print(a[3])
print(a[2]+a[4])
print(a[2:4])
print("Data type")
print(a.dtype)
#Access 2D arrays
a=np.array([[1,2,3],[6,7,9],[8,9,8]])
print(a.shape)
print(a[1,2])
print(a[2,-1])
print(a[1,1:3])
print(a.dtype)
# S indicates string
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr.dtype)
# Copy
print('Copy')
#changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
a=np.array([90,33,2,89,11,98])
print(a)
x=a.copy()
print(x)
# Base (To know whether data is owned by copy or not)
print(x.base)
# change value in copy
x[2]=99999
print(x)
print(a)  # original array is same
# View
print("View")
# reverse of copy
x=a.view()
print(x)
print(x.base)
print(a)
x[0]=10000
print(x)
print(a)   # original array is changed
# Shape of array
print('Shape')
print(a.shape)
# Reshaping an array
print("Reshaping an array")
# 1D to 2D
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
# 1D to 3D
newarr = arr.reshape(2, 3, 2)
print(newarr)
# Flattening the arrays(from multi dimension to 1D)
print("Flattening of arrays")
a=np.array([[1,2,3],[4,5,6]])
print(a.ndim)
# To reshape use -1
arr=a.reshape(-1)
print(arr)
# Array Iterating
print("Array Iterating")
b=np.array([1,2,3,4,5,6,7,8,9,10])
# 1D array
for i in b:
    print(i)
# 2D array
for i in a:
    print(i)
# 3D array
c=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for i in c:
    print(i)
# reiterating 3D to get 1D
for i in c:
    for j in i:
        print(j)

# again reiterating to get 0D
for i in c:
    for j in i:
        for k in j:
            print(k)
# Use nditer() to directly get values
print("nditer()")
for i in np.nditer(c):
    print(i)

# Using 1D array to change the datatype of values while iterating
a=np.array([1,2,3])
for i in np.nditer(a,flags=['buffered'],op_dtypes=['S']):
    print(i)
    print(i.dtype)

print("Concatenation of arrays:")
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

# 2D arrays
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
# axis=1 along row
arr=np.concatenate((a,b),axis=1)
print(arr)
# by default axis=0 along columns
arr=np.concatenate((a,b))
print(arr)
# using stack function
print("Stack function")
arr=np.stack((arr1,arr2),axis=1)
print(arr)
# stacking along rows
arr=np.hstack((arr1,arr2))
print(arr)
# stacking along columns
arr=np.vstack((arr1,arr2))
print(arr)
# stacking along depth
arr=np.dstack((arr1,arr2))
print(arr)

# Splitting arrays
print("Splitting arrays")
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(type(newarr))
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
# split along rows
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
# using of hsplit
newarr = np.hsplit(arr, 3)
print(newarr)
# Searching arrays
print("Searching arrays")
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)
# find the indices where values are even
x=np.where(arr%2==0)
print(x)
print("Search Sorted")
arr=np.array([6,7,8,9])
x=np.searchsorted(arr,7)
print(x)
# From right
x=np.searchsorted(arr,7,side='right')
print(x)
# Multiple values
arr=np.array([1,3,5,7])
x=np.searchsorted(arr,[2,4,6])
print(x)
# Sorting Arrays
print("Sorting Arrays")
arr=np.array([3,2,0,1])
print(np.sort(arr))
# Sorting 2D array
arr=np.array([[3,2,4],[5,0,1]])
print(np.sort(arr))

