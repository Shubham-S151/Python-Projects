line="the length of a string can be find using len() function as it is depicted below"
l=len(line)
print(l)
# string slicing mean that when we wnat to get just get the necessary part of string then use string slicing
# below the method is used to print the part of string we wanted
name = "Shubham"
print(name[0:7])
print(name[0:6])
print(name[4:7])
print(name[1:7])
# when we use slicing then we have to start with 0 and go upto n but the result we get is upto (n-1)th string as shown above
print(name[:])
print(name[:7])
# the above two example are used for printing the same string
# the below function give the same result as the print(name[0:6]) that means weather we apply 0 or not in front is same
print(name[:6])
# negative slicing in python
print(name[0:-5])
# now the above function is treated as print(name[0:len(name)-5]) try to run this also
# print(name[-1,-5]) this throws an error because this is interpreted as [6:2] which is not possible
print(name[-5:-1])
# the above code run because it is interpreted as [2:6]
# we can also acess the specific character of a string as shown above
print(name[6])
