# import sys
#list method

# my_list=[2,4,6,8]
# print(my_list[2])
# my_list.append(12)
# print(my_list)
# my_list.remove(6)
# print(my_list)
# my_list.pop()
# print(my_list)
# del my_list[2]
# print(my_list)

list2=["sumit",'abhishek',
       'abhay',"irfan"]
print(list2)  #print your list

print(type(list2)) #print type of the list

list2.sort()   #print sort form of list
print(list2)

list2.insert(2,"anuj") #insert  a stringe on index no.2
print(list2)

list2.sort()   #again print sort form of list
print(list2)

marks=[3,5,6,9,6,"ak"]
print(marks[-3])
print(marks[len(marks)-3])
print(marks[6-3])
print(marks[3])
# print(len(marks))

if 5 in marks:
       print("yes")
else:
       print("no")


#list comprehension
lst=[i for i in range(100) if (i%2==0)]
print(lst)

# for j in range(30):
#        if(j%2==0):
#               print(j)

# print(sys.getsizeof(marks),"byte")