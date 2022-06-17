#43. Accept the age, sex (‘M’, ‘F’), number of days and display the wages 
# accordingly If age does not fall in any range then display the 
#following message: “Enter appropriate age”

day=int(input("take days"))
age=int(input("take age"))
sex=input("take sex")
if age>=18 and age<30 and sex=="M":
    print("M-person total wages=",day*700)
elif age>=18 and age<30 and sex=="F":
    print("F-person total wages=",day*750) 
elif age>=30 and age<=40 and sex=="M":
    print("M-person total wages=",day*800) 
elif age>=30 and age<=40 and sex=="F":
    print("F-person total wages=",day*850)
else:
    print("not")          