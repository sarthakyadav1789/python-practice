a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

print("add\t:\taddition\nsub\t:\tsubtraction\nprod\t:\tmultiplication\ndiv\t:\tdivision")
func=input("Enter the function to be performed :")

if func=="add" :
    print("Result : ", a+b)
elif func=="sub" :
    print("Result : ", a-b)
elif func=="prod" :
    print("Result : ", a*b)
elif func=="div" :
    print("Result : ", a/b)