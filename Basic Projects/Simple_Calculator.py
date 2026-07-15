# Simple calculator in python without inbuilt functions

# menu
def menu():
    """Call this function to print the menu to console"""
    m = "Please select the operation from the following:\n1 >> Addition\n2 >> Substraction\n3 >> Multiplication\n4 >> Division\n5 >> Floor Division \
    \n6 >> Power\n7 >> Exit"
    return m

# take user input
def uinput():
    num1 = float(input("Enter you number1: "))
    num2 = float(input("Enter you number2: "))
    return num1, num2

# Adding 2 numbers 
def add(a,b):
    return a+b

# substracting 2 numbers 
def subs(a,b):
    return a-b

# Multiplication 2 numbers 
def mul(a,b):
    return a*b

# Division 2 numbers 
def div(a,b):
    return a/b

# Floor Division 
def floor_div(a,b):
    return a//b # int(a/b)

# raise a number to a power
def pow(a,b):
    return a**b # raise a to power b

# main_loop
while True:
    print("Welcome to Excited Nuclei Channel !\n")
    print(menu(),'\n')
    opt = int(input("Write your choice here: "))
    # print('\n')
    if opt == 7:
        print("Thanks for using this calculator !")
        break
    else :
        if opt < 7:
            num1, num2 = uinput()
            if opt == 1:
                print(f"Adding {num1} and {num2} result in: {add(num1,num2)}\n")
            elif opt == 2:
                print(f"Substracting {num1} and {num2} result in: {subs(num1,num2)}\n")
            elif opt == 3:
                print(f"Multiplying {num1} and {num2} result in: {mul(num1,num2)}\n")
            elif opt == 4:
                print(f"Dividing {num1} by {num2} result in: {div(num1,num2)}\n")
            elif opt == 5:
                print(f"Floor Dividing {num1} by {num2} result in: {floor_div(num1,num2)}\n")
            elif opt == 6:
                print(f"Raising {num1} to {num2} power result in: {pow(num1,num2)}\n")
        else :
            print("Invalid Option!, Please Choose Again.")