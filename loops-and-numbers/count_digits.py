# Program to count the number of digits in a number

num = int(input("Enter a number : "))

if num == 0:
    count = 1
else:
    count = 0
    num = abs(num)   # handle negative numbers
    while num > 0:
        count += 1
        num //= 10

print(f"Number of digits in number : {count}")
