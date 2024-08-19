operator=input("select an operator(+,-,*,/) :")
num1=float(input("enter 1st number :"))
num2=float(input("enter 2st number :"))

if operator=="+":
     ans=num1+num2
elif operator=="-":
    ans=num1-num2
elif operator=="*":
    ans=num1*num2
elif operator=="/":
    ans=num1/num2
print(ans)