#50. Write a Python program that reads two integers representing a month 
# and day and prints the season for that month and day.
#a. Expected Output:
#Input the month (e.g. January, February etc.): julyInput the day: 31
#Season is autumn

month=input("enter month")
day=int(input("enter day"))
if month=="march"or month=="april"or month=="may":
    if day>=1 and day<=30 or day>=1 and day<=31:
        print("spring")
elif month=="june"or month=="july"or month=="auguset":
    if day>=1 and day<=31 or day<=30:
        print("summer")
elif month=="september"or month=="october"or month=="november":
    if day>=1 and day<=30 or day<=31:
        print("autumn")
elif month=="december"or month=="junuary"or month=="february":
    if day>=1 and day<=28 or day<=30 and day<=31:
        print("winter") 
else:
    print("not")                       