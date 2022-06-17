#25. A student will not be allowed to sit in an exam if his/her attendance 
#is less than 75%.Take following input from the user. Number of classes held.
#Number of classes attended. And print, percentage of class attended.
# Is the student is allowed to sit in the exam or not.

held=int(input("enter classes held"))
attend=int(input("enter class attendend"))
percen=attend*held//100
if percen<75:
    print("percentage of class attended=",percen,"no allowed for exam")
else:
    print("percentage attended=",percen,"alowed for exam")    