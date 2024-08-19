def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(6))

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

def natural(n):
    if(n==0):
        return 0
    return natural(n-1)+n
sum=natural(5)
print("sum of natural numbers",sum)

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["mango","apple","banana","litchi"]
print_list(fruits)