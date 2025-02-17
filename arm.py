print("if you want to write a three digit number and check if it is")
num1=int(input("enter the first digit with two zeros"))
num2=int(input("enter the second digit with one zero"))
num3=int(input("enter the third digit"))
ognum=num1+num2+num3
num4=num1/100
num5=num2/10
print("your number is ",ognum)
if(num4**3+num5**3+num3**3==ognum):
    print("the number is a armstrong number")
else:
    print("the number is not a armstrong")