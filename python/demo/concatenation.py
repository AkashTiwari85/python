#string & Numeric values can operate together with '*'
a,b=4,3
txt="@"
print(a*txt*b)

#ek string ko dusri string se jodna concatenation kahte hai
#string & string can operate with '+'
c="3"
print((c+txt)*b)

#Numeric values can operate with all arithmetic operators
d=5
print(a+b*d)

#Arithmetic expression with integer and float will result in float
e=7.6
print(a*e)