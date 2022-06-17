#20. Write a python program to input electricity unit charges and calculate total
#electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

unit=int(input("enter unit"))
if unit>=1 and unit<=50:
    a=unit*0.50+20/100
    print("bill=",a)
elif unit>50 and unit<=151:
    a=unit*0.75+20/100
    print("bill=",a)
elif unit>151 and unit<=251:
    a=unit*1.20+20/100
    print("bill=",a)
elif unit>250:
    a=unit*1.50+20/100
    print("bill=",a)         