f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

#write mode
f=open("demo.txt","a")
data=f.write("I am learning python")
print(data)
f.close()
#open file -with
with open("demo.txt","w") as f:
    data=f.write("new data")
    print(data)

#deleting a file //using the os module
# import os
# os.remove("demo.txt")

#question
with open("practice.txt","w") as f:
    print("Hi everyone\n we are learning I/O")
    print("using java.\n I like programming in java")

#replace with python
with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    data=f.write(new_data)
    