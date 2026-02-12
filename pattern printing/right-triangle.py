# Program to print a right angled triangle

num=int(input("Enter the length of pattern :"))

for i in range(1,num+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
