# string is something that is enclosed in "_" or '_' (double or single quotations)
name='Shubham'#it is a string
friend1="sachin"
friend2="panlkaj"
friend3='sagar'
print("my name is ",name,'and my friends are',friend1,',',friend2,"and",friend3)
print("he said that,'i want to eat an apple'")
print(' he said that ," iwant to eat an apple"')
apple="he said that,\"i want to eat an apple\""
print(apple)
apple1='he said that,"i waant to eat an apple"'
print(apple1)
# multiline strings can be executed using '''____''' or """___"""
s='''he said,
hi Shubham
how are you doing ?'''
print(s)
# while indexing the string started with 0 to (n-1)th character
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# print(name[7]) throws error as there is no 8th string
# looping in string  is the easy method of indexing is 'looping in strings'
for character in s :
    print(character)