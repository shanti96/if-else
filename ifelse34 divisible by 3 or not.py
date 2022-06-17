#34. Write a program to check whether the last digit of a number
# ( entered by user ) is divisible by 3 or not.

num=int(input("enter a number"))
b=num%10
if b%3==0:
    print("last digit=",b,"divisible by 3")
else:
    print("not divisible by 3")    