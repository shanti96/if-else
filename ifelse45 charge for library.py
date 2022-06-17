#45. Accept the number of days from the user and calculate the charge for
#  library according to following :
#First five days : Rs 2/day.
#Six to ten days : Rs 3/day.
#Ten to 15 days : Rs 4/day
#After 15 days : Rs 5/day

day=int(input("take the days"))
if day>=1 and day<=5:
    print("charge for library=",day*2)
elif day>=6 and day<=10:
    print("charge for library=",day*3) 
elif day>=10 and day<=15:
    print("charge for library=",day*4) 
elif day>15:
    print("charge for library=",day*5)      