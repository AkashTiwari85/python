tpl=("Spain","Italy","India","England","Germany")
temp=list(tpl)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
tpl=tuple(temp)
print(tpl)