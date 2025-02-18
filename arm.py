print("if you want to write a three digit number and check if it is")
num1=int(input("enter the first digit"))
num2=int(input("enter the second digit"))
num3=int(input("enter the third digit"))
num4=num1*100
num5=num2*10
ognum=num4+num5+num3
print("your number is ",ognum)
if(num1**3+num2**3+num3**3==ognum):
    print("the number is a armstrong number")
else:
    print("the number is not a armstrong")