#9. Write a python program to input any character and check whether 
# it is alphabet,digit or special character.
cha=input("enter the number")
if cha>='A'and cha<='Z'or cha>='a'and cha<='z':
    print("alphabet")
elif cha<='9'and cha>='0':
    print("digit") 
else:
    print("special character")       