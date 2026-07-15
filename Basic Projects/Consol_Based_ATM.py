# Project : Consol based ATM 
# it is going to show the balance, allow user to deposit money, allow to withdraw money, Exit
user= {"User":"Shubham",
       "Balance": 200000}

# greet the user
def greet(user:dict):
    return f"Welcome {user.get("User")}!, to EN Banking Services"

# Balance Check
def check_bal(user:dict):
    return user.get("Balance")

# deposit
def deposit(user:dict, bal:int, amt:int):
    bal+=amt
    user['Balance'] = bal
    return bal

def withdraw(user:dict, bal:int, amt:int):
    if amt>bal:
        print("Invalid Amount Entered !\nPlease Try again.")
    else :
        bal-=amt
        user['Balance'] = bal
    return bal

# main Loop
while True:
    print(greet(user))
    print(f"\nPlease Select the Operation: \n1 >> Checking Balance\n2 >> Deposit\n3 >> Withdraw\n4 >> Exit")
    opt = int(input("Please Enter Your Choice: "))
    # print(user.keys())
    name,balance = user.values()
    balance= int(balance)
    if opt == 1:
        print(f"Your Balance is: {check_bal(user)}")
    elif opt == 2:
        amt = int(input("Enter the amount you want to deposit: "))
        balance = deposit(user,balance, amt)
        print(f"Your transaction is successful. Your new balance is: {balance}")
    elif opt == 3:
        amt = int(input("Enter the amount you want to withdraw: "))
        balance = withdraw(user,balance, amt)
        print(f"Your transaction is successful. Your new balance is: {balance}")
    elif opt == 4:
        print("Thanks for using our services")
        break
    else :
        print("Invalid! Option Selected Please try again.")