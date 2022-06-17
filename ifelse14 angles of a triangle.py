#14. Write a python program to input angles of a triangle and 
# check whether triangle is valid or not.
a=int(input("take a angles number"))
b=int(input("take a second angles"))
c=int(input("take a third angles"))
if a+b+c==180:
    print("valid triangle")
else:
    print("not")    