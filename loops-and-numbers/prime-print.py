def prime(num):
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            break
    else:
        return num

x = int(input("Enter a number :"))

for i in range(2,x+1):
    if prime(i):
        print(i)