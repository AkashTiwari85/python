#we can not change
mytuple=(2,5,6,8,"ak",6,2,1)
print(type(mytuple))

type(mytuple)
print(mytuple)

print(mytuple[2])

print(len(mytuple))

if 6 in mytuple:
    print("yes")
else:
    print("no")

print(mytuple.count(6))

mylist=list(mytuple)
print(mylist)
print(type(mylist))

import sys
mylis = [0,1,2,"hello",True]
mytup = (0,1,2,"hello",True)
print(sys.getsizeof(mylis),"byte")
print(sys.getsizeof(mytup),"byte")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))