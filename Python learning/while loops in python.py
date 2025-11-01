count=-10
while count>0:
    print(count)
    count-=1
else :
    count+=1
    print(count)
# difference between for loops and while loops is that in while loops we have to predefine a value
n=int(input('enter the number:'))
while n<=40:
    n=int(input('enter the number:'))
    print(n)
print('done with the loop')
# else statement with while loop
x=5
while x>0:
    print(x)
    x-=1
else:
    print('counter is 0')
# do- while loop in python 
while True:
    number=int(input('enter a positive number:'))
    print(number)
    if not number>0:
        break