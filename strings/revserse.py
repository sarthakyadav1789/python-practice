# Program to reverse a string

string = input("Enter a string :")
print("The original string is :",string)

rev = ""
for i in range(1,len(string)+1):
    rev+=string[len(string)-i]

print("The reversed string is :",rev)