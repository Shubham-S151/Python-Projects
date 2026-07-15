# Project: Password Strength Checker
# This beginner level project is gong to be the beginner level project that helps user check the 
# strength of the password by checking some conditions.

# Conditions :
# 1. length of password must be >= 8
# 2. must contain at least one upper case chaacter
# 3. must contain at least one lower case chaacter
# 4. must have at least one special character
# 5. must have at least one number in it
# 6. does not have the name of user in it

# length check 
def length_check(password:str) -> bool:
    """This function is going go take password and check its length"""
    return len(password) >= 8

# upper case character check
def upper_case_check(password:str) ->bool:
    """This function is going go take password and check weather it conatins upper case char or not"""
    for i in password:
        if i.isupper():
            return True
    return False

# upper case character check
def lower_case_check(password:str) ->bool:
    """This function is going go take password and check weather it conatins lower case char or not"""
    for i in password:
        if i.islower():
            return True
    return False

# special character character check
def special_char_check(password:str) ->bool:
    """This function is going go take password and check weather it conatins special character or not"""
    for i in password:
        if not i.isalnum(): # alnum >> [a-z,A-Z,0-9]
            return True
    return False

# special character character check
def num_check(password:str) ->bool:
    """This function is going go take password and check weather it conatins special character or not"""
    for i in password:
        if i.isnumeric():
            return True
    return False
    
# name check
def name_check(password:str, name:str) -> bool:
    """Checks weather password conatins name or not"""
    return name.lower() in password.lower()

# scoring of password
def score(password:str, name:str) -> int:
    """Gives score based on the checks"""
    sco = 0
    sco += int(length_check(password))
    sco += int(upper_case_check(password))
    sco += int(lower_case_check(password))
    sco += int(num_check(password))
    sco += int(special_char_check(password))
    sco -= int(name_check(password,name))
    return sco

name = input("Enter Your Name: ")
password = input("Enter Your Password: ")
scre = score(password,name)

print("===============Password Analysis===============")
print(f"Password: {password} rated {scre}/5")
if scre <=2:
    print("Passowrd is weak")
if 2< scre <=4:
    print("Passowrd is moderate")
if scre ==5:
    print("Passowrd is strong")

print("=================Recomendations=================")
if not length_check(password):
    print("- Password should be at least 8 characters long")
if not upper_case_check(password):
    print("- Add at least one uppercase letter")
if not lower_case_check(password):
    print("- Add at least one lowercase letter")
if not num_check(password):
    print("- Add at least one number")
if not special_char_check(password):
    print("- Add at least one special character (!,@,#,$ etc.)")
if name_check(password,name):
    print("- Do not include your name in the password")