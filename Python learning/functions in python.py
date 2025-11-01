# to write any user defined function we start it by def as shown below
def name(fname,lname):
    print("hello,",fname, lname)
name("Shubham","Sharma")
print(name)
# as we have seen above to create a function we have to start with def and then name the function that
# we are trying to create and in the parenthesis we defines the variables 
# to call a function that we have created we have to type the name of that function and the value
# of the variables in the parenthesis 
def isgreater(a,b):
    if a>b:
        print(a,'is greater than',b)
        print('the difference of a&b is:',a-b)
    else:
        print(a,'is lesser than',b)
        print('the sum of a&b is:',a+b)
a=20
b=10
isgreater(a,b)
# the other method to call a function
isgreater(10,30)
