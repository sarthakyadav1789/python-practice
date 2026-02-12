# Program to print fibonacci sequence

num=int(input("Enter the number of terms of fibonacci sequence to be printed :"))

if num <= 0:
    print("Invalid input")
elif num == 1:
    print([0])
elif num == 2:
    print([0, 1])
series=[0,1]
for i in range(0,num):
    term=series[-1]+series[-2]
    series.append(term)

for i in series:
    print(i)