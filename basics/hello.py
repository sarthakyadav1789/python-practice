# This is a code to show how output can be formatted in python in various ways.

mesg = "Hello World"

# This is simple print
print(mesg)

# This is using string modulo operator
print("The message is : %s"%(mesg))

# Using format() method
print("The message is : {0}".format(mesg))

# Advanced formatting using format 5d,3d,7d shows how much digit space should be given for the variable.
print("The variables are  : {0:5d},{1:3d} and {2:7d}".format(23,45,67))

# using string method
print(mesg.center(40,"-"))
print(mesg.ljust(40,"-"))
print(mesg.rjust(40,"-"))