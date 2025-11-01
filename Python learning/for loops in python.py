# for loops
n='shubham'
for i in n:
    print(i)
# second form
for i in n:
    print(i,end=",")
print('\n for statement for list')
# for statement in list
c=['red','yellow','green','blue']
for i in c:
    print(i)
    for j in i:
        print(j)
print('\n')
# use of range function
for k in range(5):
    print(k+1) # if we only use k in here it will print 0-8
print('\n setting start and end in range')
for k in  range(1,9):
    print(k)
print('\n setting start and end in range with the gap')
for k in range(0,10,2):
    print(k)