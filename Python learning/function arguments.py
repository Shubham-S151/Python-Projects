def average(a,b):
    print('average is :',((a+b)/2))
average(4,6) 
# there are four types of arguments
# 1. default argument
print('examples of default arguments')
def name(fname,mname='jhon',lname='whatson'):
    print('hello,',fname,mname,lname)
name('Amy')
name('Amy','will')
name('Shubham','Vashist','Sharma')
def average(a=5,b=4):
    print('average is :',((a+b)/2))
average()
average(3,8)#if the value of variables are defined then the function will consider those values
average(2)#if we give valus like this than the value given will be considered as first value 
# and 2nd remain default
average(b=8)# in this second is given but first will be default

# 2. keyword argment
print('examples of keyword arguments')
def average(a,b):
    print('average is :',((a+b)/2))
average(b=2,a=11)
def name(fname,mname,lname):
    print('hello,',fname,mname,lname)
name(mname='vashist',lname='sharma',fname='shubham')

# 3. required arguments
print('examples of required arguments')
def average(a,b=10):
    print('average is :',((a+b)/2))
average(1)
# average(b=4)# throws an error
average(23,12)# here a is an required argument

# 4. variable length arguments
print('examples of variable length arguments')
def average1(*numbers):
    print(type(numbers))
    print(numbers)
    sum=0
    for i in numbers:
        sum=sum+i
        # print('average is :',sum/len(numbers))
        # if we use the above method then we get all the averages with the numbers given as input
        # because it lies in the loop statement
    # print('average is :',sum/len(numbers))
    return sum/len(numbers)
# the return and print gives the same result but
# print also gives the information on functions in (def function)
a=average1(5)
b=average1(6,8)
c=average1(1,2,3,4)
print(a)
print(b)
print(c)
def name(*name):
    print('hello,',name[0],name[1],name[2])
name('shubham','vashist','sharma')

# return statement
# it is used to return the value of the expression block to the calling function
def name(fname,mname,lname):
    return 'hello,'+fname+' '+mname+' '+lname
print(name('Shubham','vashist','sharma'))

# keyword arbitrary arguments
def name(**name):
    print(type(name))
    print('hello,',name['fname'],name['mname'],name['lname'])
    # this takes input as dictionary
name(fname='shubham',mname='vashist',lname='sharma')