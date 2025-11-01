a=int(input("enter your age:"))
print('your age is ',a)
# the space after if and else is called identation and it represents the starting of block
if a>=18:
    print('you are eligile for vote')
else :
    print('you are not eligible for vote')
# conditional operators includes <, >, <=, >=, ==, !=, 
'''print(a==18)
print(a>=18)
print(a<=18)
print(a!=18)
print(a<18)
print(a>18)
#try to run above statement after removing quotes '''
# elif is used when we are dealing with more than 2 conditions
appleprice=190
budget=200
if budget - appleprice >= 50:
    print("you have enough money left")
elif budget-appleprice>= 70:
    print("you have enough apples")
else :
    print("your budget is low")
num1=19
if num1<0:
    print('number is negative')
elif num1>0:
    if num1>0 and num1<10:
        print('number lies between 1-10')
    elif num1>10 and num1<20 :
        print('number lies between 11-20')
    else:
        print('the number is positive')
else:
    print('the number is 0')
# next is while loop