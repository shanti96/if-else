#22. A company decided to give a bonus of 5% to an employee if his/her year
#  of service is more than 5 years. Ask users for their salary and 
# year of service and print the net bonus amount.

salary=int(input("take salary"))
year=int(input("take year"))
if year>5:
    bonus=salary*5/100
    amount=bonus+salary
    print("total 5% bonus=",amount)
else:
    print("no bonus only salary=",salary)    