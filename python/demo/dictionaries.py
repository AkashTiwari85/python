#like "ak" ek key hai jiske undar hm value ko store kr rhe hai
dic={
    "Ak":"Human being",
    "Spoon":"Object",
    1:"Karan",
    2:"sumit",
    3:"Anuj",
}
print(dic["Ak"])  #return the key according to value
print(dic[3])

print("get.:--",dic.get("tiwari"))

dic.update({4:"shivam"})
print("after update:--",dic)

print("keys :--",dic.keys())  #return all the keys
print("values :--",dic.values())  #return all the values
print("items :--",dic.items())

#null dic
null_dic={}
null_dic["name"]="aktiwari"
print(null_dic)

#nested dic
student={
    "name":"aktiwari",
    "subject":{
        "phy":98,
        "chem":87,
        "math":99
    }
}
print(student["subject"]["math"])

#mydict
mydict={
    "name":"max",
    "age":28,
    "city":"NewYork"
}
print(mydict)
print(mydict["age"])

mydict["email"]="ak@gmail.com"
print(mydict)

for key,value in mydict.items():
    print(key,value)