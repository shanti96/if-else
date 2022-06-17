#44. Accept three numbers from the user and display the second largest number.

a=int(input("take a number"))
b=int(input("enter a number"))
c=int(input("take a number"))
if a>b and b>c or a<b and c>b:
    print("b is second largest number")
elif a>b and a<c or a>c and a<b:
    print("a is second largest number")
elif a>c and c>b or a<c and c<b:
    print("c is second largest number")
else:
    print("no are second largest number")            