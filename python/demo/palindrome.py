from typing import List

list1=[1,2,8]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrom")
else:
    print("not")