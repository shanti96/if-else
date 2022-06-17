#35. Write a program to accept the cost price of a bike and display the 
# road tax to be paid according to the following criteria :
#a.Cost price (in Rs)             Tax

#b.> 100000                       15%
#c.> 50000 and <= 100000          10%
#d.<= 50000                       5%

cost_price=int(input("enter price"))
if cost_price>100000:
    a=cost_price*15/100
    print("rode tax=",a)
elif cost_price>50000 and cost_price<=100000:
    a=cost_price*10/100
    print("rode tax=",a) 
elif cost_price<=50000:
    a=cost_price*5/100
    print("rode tax=",a)
else:
    print("not")               