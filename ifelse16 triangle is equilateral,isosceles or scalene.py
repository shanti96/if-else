#16. Write a python program to check whether the triangle 
# is equilateral, isosceles or scalene triangle.
a=int(input("take number"))
b=int(input("take number"))
c=int(input("take a number"))
if a==b and b==c:
    print("equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print("scalene")        