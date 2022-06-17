#51.Write a Python program to find the median of three values. Go to the
#editor
#i. Expected Output:
#ii. Input first number: 15
#iii. Input second number: 26
#iv. Input third number: 29
#v. The median is 26.0

a=int(input("enter number"))
b=int(input("enter second number"))
c=int(input("enter threed number"))
if a>b and b>c or c>b and b>a:
    print(float(b))
elif a>c and c>b or b>c and c>a:
    print(float(c)) 
elif c>a and a>b or b>a and a>c:
    print(float(a))
else:
    print("not")           