a=int(input("enter the number :"))
factorial=1
if a>=0:
    for i in range(1,a+1):
        factorial=factorial*i
        print("factorial of given number",factorial)