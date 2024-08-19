num=int(input("Enter the value of num: "))
if(num<0):
    print("Number is negative.")
elif(num==0):
    print("Number is zero")
elif(num==90):
    print("Number is special.")
else:
    print("Number of positive.")

#traffic light code

light=input("light: ")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

marks=int(input("enter your marks: "))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D")
