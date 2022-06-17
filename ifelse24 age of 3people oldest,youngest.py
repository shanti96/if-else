#24. Take the age of 3 people by user and determine oldest and 
# youngest among them.

a=int(input("take age"))
b=int(input("take age"))
c=int(input("take age"))
if a>b and a>c and c<b:
    print("oldest=a",a,"youngest=c",c)
elif a>b and a>c and b<c:
    print("oldest=a",a,"youngest=b",b) 
elif b>a and b>c and a<c:
    print("oldest=b",b,"youngest=a",a) 
elif b>a and b>c and c<a:
    print("oldest=b",b,"youngest=c",c)
elif c>a and c>b and a<b:
    print("oldest=c",c,"youngest=a",a) 
elif c>a and c>b and b<a:
    print("oldest=c",c,"youngest=b",b) 
else:
    print("no are oldest and youngest")                    