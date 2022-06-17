#33. Write a program to display the last digit of a number.

num=int(input("[enter the number"))
i=num%10
if num%10>=0:
    print("last digit number=",i)
else:
    print("not last digit")    