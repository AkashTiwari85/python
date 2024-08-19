#same values are remove automatic

s={1,2,3,4}
s1={4,5,6}
print("union:--",s.union(s1))

s.update(s1)
print("update:--",s,s1)

s2=s.intersection(s1)
print("intersection:--",s2)

s3=s.symmetric_difference(s1)
print("symmetric_difference:--",s3)

s4=s.difference(s1)
print("difference:--",s4)

s1.add(9)
print("add:--",s1)

s1.remove(6)
print("remove:--",s1)

print("type:--",type(s))

print("length:--",len(s1))

# s4=s.pop(s1)
# print(s1)



set1={
    "pyhon","java","c++","python","javascript","java","python","java","c++","c"
}
print(set1)
print(len(set1))
