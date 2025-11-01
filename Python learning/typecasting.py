a="1"
# a=1
b="2"
# b=2
print(a+b)#in this we try to convert a,b into integers but they stay as string
print(int(a)+int(b))# in this the int function change string into integer then execute addition
""" the data type in which we are changing the specified "data type" the 
entry must be valid data type so that type-cast must be executable """
# implicit type casting
c = 0.9
d = 8
print("c=0.9")
print("d=8")
print("type of c", type(c))
print("type of d",type(d))
print(c+d)
print("type of c+d",type(c+d))
# here the c is float and d is integer and c+d convert into float 