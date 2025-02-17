total=int(input("enter the total days of school"))
attendence=int(input("enter the number of days you were present"))
percent=(attendence/total)*100
if(percent<=70):
    print("your attendence is perfect")
else:
    print("your attendence is not good")