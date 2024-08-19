l=[1,9,3,4,6]
print("list",l)
l.append(8)
print("append",l)

l.sort()
print("sort",l)

l.reverse()
print("reverse",l)

print(l.index(4))
print("index number 4",l)

print(l.count(1))
print("count",l)

m=l.copy()
m[0]=0
print("copy:",l)

l.insert(1,5)
print("insert:",l)

l.clear()
print("clear",l)

# l.slice(2,3)
# print("slice",l)

l1=[6,7,8,9]
l1.extend(l)
print("extend function",l1)

l1.remove(6)
print(l1)

