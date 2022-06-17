#40. Write a program to check whether a number entered is a three digit 
# number or not.

num=int(input("take a number"))
if num>=100 and num<=999:
    print("num is a three digit number",num)
else:
    print("not three digit number",num)    