# This code is to show how can you swap to numbers.
# I know 3 ways in python

print("    Method 1    ".center(60,"="))
# Using multiple assignment in 
a = 10
b = 20
print("value of a is : {0} and value of b is : {1} | Before SWAP".format(a,b))
a,b = b,a
print("value of a is : {0} and value of b is : {1} | After SWAP".format(a,b))

print("    Method 2    ".center(60,"="))
# using a temporary variable
a = 10
b = 20
print("value of a is : {0} and value of b is : {1} | Before SWAP".format(a,b))
temp = b
b = a
a = temp
print("value of a is : {0} and value of b is : {1} | After SWAP".format(a,b))

print("    Method 3    ".center(60,"="))
# Using adddition
a = 10
b = 20
print("value of a is : {0} and value of b is : {1} | Before SWAP".format(a,b))
b=a+b
a=b-a
b=b-a
print("value of a is : {0} and value of b is : {1} | After SWAP".format(a,b))
