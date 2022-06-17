#32. Write a program to calculate the electricity bill (accept number of 
# unit from user)according to the following criteria :
#Unit               Price
#First 100 units     no charge

#Next 100 units      Rs 5 per unit

#After 200 units     Rs 10 per unit

#(For example if input unit is 350 than total bill amount is Rs2000)

unit=int(input("enter unit"))
if unit>0 and unit<=100:
    print("electricity bill=","no charge")
elif unit>100 and unit<=200:
    print("electricity bill=",(unit-100)*5)
else:
    a=unit-100
    b=100*5
    c=a-100
    d=c*10
    print("electricity bill=",b+d)            