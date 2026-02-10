# This code shows how to read an integer,a float and a string from user

# the program throws an error if your enter a string in place of integer
# An integer is auto matically changed to float but a string throws error
# No str() needed as default input type is string only.

num1 = int(input("Enter the integer :"))
print(f"The integer is : {num1}")

flt1 = float(input("Enter the floating point number :"))
print(f"The float is : {flt1}")

str1 = input("Enter the string : ")
print(f"The string is : {str1}")