a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>=b and a>=c):
    print(a,"a is greatest number")
elif(b>=c):
    print(b,"b is greatest number")
else:
    print(c,"c is a greatest number")