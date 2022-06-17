#Write a python program to find maximum between three numbers.
num1=int(input("enter the number"))
num2=int(input("enter the second number"))
num3=int(input("enter a third number"))
if num1>num2 and num1>num3:
    print("num1 is maximum number")
elif num2>num1 and num2>num3:
    print("num2 is maximum number")
elif num3>num1 and num3>num2:
    print("num3 is maximum number")    
else:
    print("not are maximum number")        