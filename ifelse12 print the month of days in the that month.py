#12. Write a python program to input the month number and print 
# the number of days in that month.
month=int(input("enter the month number"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31 days")
elif month==4 or month==6 or month==9 or month==11:
    print("30 days")
elif month==2:
    print("28 days")
else:
    print("non")            