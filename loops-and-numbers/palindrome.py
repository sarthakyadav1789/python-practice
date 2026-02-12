# Program to check palindrome

num = int(input("Enter a number to be checked :"))
rev=0
org = num

print(f"The original number is : {num}")

while(num>0):
    temp=num%10
    rev=(rev*10)+temp
    num=num//10

if org==rev :
    print(f"The number {org} is a palindrome.")
else :
    print(f"The number {org} is not a palindrome.")