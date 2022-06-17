#6. Write a python program to check whether a year is leap year or not
year=int(input("enter a year"))
if year%4==0 and year%100!=0:
    print("leap year")
elif year%100==0 and year%400==0:
    print("leap year an century year")
else:
    print("not leap year")    
