# Program to reverse a number

num = int(input("Enter a number to be reversed :"))
rev=0

print(f"The original number is : {num}")

while(num>0):
    temp=num%10
    rev=(rev*10)+temp
    num=num//10

print(f"The reversed number is : {rev}")