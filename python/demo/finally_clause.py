
try:
    l=[3,4,5,6]
    i=int(input("enter the index:"))
    print(l[i])
except:
    print("some error occurred")
finally:
    print("i am always executed")