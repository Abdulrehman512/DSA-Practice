from array import *

array1 = array('i',[10,20,30,40,50])

for x in array1:
    print(x)

# Accessing through index

print(array1[0])
print(array1[1])
print(array1[2])
print(array1[3])
print(array1[4])

# Insertion

array1.insert(2,77)

print(array1)

# Deletion

array1.remove(40)

print(array1)