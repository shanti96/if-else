#48. Write a Python program to sum of two given integers. However, if the
#  sum is between 15 to 20 it will return 20.

a=int(input("take a number"))
b=int(input("take a number"))
c=a+b
if c>=15 and c<=20 :
    print(20)
else:
    print("not")    