#21. A shop will give a discount of 10% if the cost of the purchased 
# quantity is more than 1000. Ask the user for quantity, Suppose,
#one unit will cost 100. Judge and print total cost for user.

quantity=int(input("take quantity"))
total_cost=quantity*100
if total_cost>1000:
    unit=total_cost*10/100
    cost=total_cost-unit
    print("total cost 10% discount=",cost)
else:
    print('only total cost=',total_cost)    