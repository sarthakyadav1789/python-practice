# Program to check a leap year

year = int(input("Enter the year to check if it is leap or not :"))

if (year%100)==0 :
    if year%400==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
elif year%4==0 :
    print(f"{year} is a leap year")
else :
    print(f"{year} is not a given year")