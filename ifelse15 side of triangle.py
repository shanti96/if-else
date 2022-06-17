#15. Write a python program to input all sides of a triangle and check 
# whether the triangle is valid or not.
a=int(input("take angles number"))
b=int(input("take second angles number"))
c=int(input("take third angles number"))
if a+b>c:
    print("triangle is valid")
elif a+c>b:
    print("triangle is valid")
elif b+c>a:
    print("triangle is valid")
else:
    print("not valid")            