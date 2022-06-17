#42. Write a program to accept two numbers and mathematical operators and 
# perform operation accordingly.
#Like:
#Enter First Number: 7
#Enter Second Number : 9
#Enter operator : +
#Your Answer is : 16

a=int(input("first number"))
b=int(input("enter second number"))
c=input("enter operators")
if c=="+":
    print(a+b)
else:
    print("flase")    