x=int(input('enter the number:'))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print('x is zero')
    # case with if statement
    case 4 if x%2==0:
        print('x%2==0 and case is 4')
    # empty case with if statement
    case _ if x<10:
        print('x is < 10')
     # default case will only be matched if the above cases were not matched
     #  so its basically just an elese
    case _ :
        print(x)