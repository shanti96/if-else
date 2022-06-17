#39. Write a program to find the lowest number out of two numbers excepted 
# from the user.

a=int(input("enter a number"))
b=int(input("enter a second number"))
if a<b:
    print("a is lowest number")
elif b<a:
    print("b is lowest number")
else:
    print("no are lowest number")        