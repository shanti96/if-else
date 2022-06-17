#17. Write a python program to calculate profit or loss.
a_cost=int(input("enter amount"))
s_price=int(input("enter amount"))
if a_cost<s_price:
    print("profit")
elif a_cost>s_price:
    print("loss")
else:
    print("no profit no loss")        