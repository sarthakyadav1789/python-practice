# Program to check armstrong number

num=input("Enter a number :")
total=0

for i in list(num):
    total+=int(i)**len(num)
if total==int(num):
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")