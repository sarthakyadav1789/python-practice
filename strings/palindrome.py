# Program to check palindrome string

data = input("Enter a string :").lower()

if data==data[::-1]:
    print("The string is palindrome.")
else :
    print("The string is not a palindrome.")