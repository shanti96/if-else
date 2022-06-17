#13. Write a python program to count the total number of notes in 
# a given amount.
amount=int(input("enter the amount"))
if amount>=5:
    a=amount//2000
    b=amount%2000
    c=b//500
    d=b%500
    e=d//200
    f=d%200
    g=f//100
    h=f%100
    i=h//50
    j=h%50
    k=j//20
    l=j%20
    m=l//10
    n=l%10
    o=n//5
    print("notes of 2000=",a,"notes of 500=",c,"notes of 200=",e,"notes of 100=",g)
    print("notes of 50=",i,"notes of 20=",k,"notes of 10=",m,"notes of 5=",o)
else:
    print("not amount")    