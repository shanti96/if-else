#46. Write a Python program to find those numbers which are divisible by 7 
# and multiple of 5, between 1500 and 2700 (both included).

a=int(input("take a number"))
if a%7==0 and a%5==0 and a>=1500 and a<=2700:
    print("a is divisible by 7 and multiple of 5",a)
else:
    print("not")    