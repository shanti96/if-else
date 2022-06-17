#18. Write a python program to input marks of five subjects Physics, Chemistry,
#Biology, Mathematics and Computer. Calculate percentage and grade according
#to following:
#Percentage >= 90% : Grade A
#Percentage >= 80% : Grade B
#Percentage >= 70% : Grade C
#Percentage >= 60% : Grade D
#Percentage >= 40% : Grade E
#Percentage < 40% : Grade F
physics=int(input("take number"))
chemistry=int(input("take mark"))
biology=int(input("take mark"))
mathematics=int(input("take mark"))
computer=int(input("enter mark"))
percen=(physics+chemistry+biology+mathematics+computer)*100//500
if percen>=90 and percen<=100:
    print("grade-A")
elif percen>=80:
    print("grade-B")
elif percen>=70:
    print("grade-C")
elif percen>=60:
    print("grade-D")
elif percen>=40:
    print("grade-E")
else:
    print("grade-F")  
print(percen)                      