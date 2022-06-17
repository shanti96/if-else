#19. Write a python program to input basic salary of an employee 
#and calculate its
#Gross salary according to following:
#Basic Salary <= 10000 : HRA = 20%, DA = 80%
#Basic Salary <= 20000 : HRA = 25%, DA = 90%
#Basic Salary > 20000 : HRA = 30%, DA = 95%
basic_salary=int(input("take salary"))
if basic_salary<=10000:
    hrd=basic_salary*20/100
    da=basic_salary*80/100
    g_s=basic_salary+hrd+da
    print("gross_salary=",g_s)
elif basic_salary<=20000:
    hrd=basic_salary*25/100
    da=basic_salary*90/100
    g_s=basic_salary+hrd+da
    print("gross_salary=",g_s)
else:
    hrd=basic_salary*30/100
    da=basic_salary*95/100
    g_s=basic_salary+hrd+da
    print("gross_salary=",g_s)