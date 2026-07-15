# Project: Number Guessing Game
# This is a beginner level project that allows to predict the number with the following hints:
# 1. Too High
# 1(a). Close but high
# 2. Too Low
# 2(a) Close but low
# 3. Close
# This game will have 3 levels :
# 1. easy difficulty   (0,100)
# 2. medium difficulty (0,500)
# 3. hell difficulty   (0,1000)
# This program is going to be using additional lobrary "Random"

import random

def random_gen(max_limit:int) -> int:
    return random.randint(0,max_limit)

def check_right_guess(guess:int, actual_num:int) -> bool :
    return guess == actual_num

def lev_range(choice:int) -> int :
    if choice == 1 : 
        print("You Choose Easy Level to Play.")
        print("I know you are scared.")
        return 100
    elif choice == 2 :
        print("You Choose Medium Level to Play.")
        print("Now you are playing.")
        return 500
    elif choice == 3 :
        print("You Choose Hell Level to Play.")
        print("I wish you all the best (LOL)!.")
        return 1000
    else :
        print("Invalid Choice!")
        print("Read the 'Menu' bro!")

def hint(ui:int , act_num:int) -> str:
    """
    Params:
        **ui**: User Input
        **act_num**: Actual Number
    Return:
        Hint the user about the guess.
    """
    if 0 < abs(ui-act_num) <= 2:
        return "You are close to actual answer."
    elif (ui > act_num) & (10 < abs(ui-act_num)):
        return "Too High"
    elif (ui > act_num) & (0 < abs(ui-act_num) <= 10):
        return "Close but High"
    elif (ui < act_num) & (10 < abs(ui-act_num)):
        return "Too Low"
    elif (ui < act_num) & (0 < abs(ui-act_num) <= 10):
        return "Close but Low"
    else:
        return "You got the Right answer"

# create a loop for replay
user_score = 0
number_replay = 0
while True:
    attempts = 5
    m = f"\nWelcome to Number Guessing Game by Excited Nuclei.\
        \nCurrent Score : {user_score} | Replays : {number_replay}\
        \nSelect the level of difficulty you want to play:\
        \nPress 1. >> Easy difficulty   Range -> [0,100]\
        \nPress 2. >> Mdium difficulty  Range -> [0,500]\
        \nPress 3. >> Hell difficulty   Range -> [0,1000]\
        \nPress 0. >> Exit"
    print(m)
    choice  = int(input("Enter your choice: "))
    if choice != 0:
        lev = lev_range(choice)
        act_num = random_gen(lev)
        for i in range(attempts):
            print(f"Attempt {i+1}/5")
            print(f"Actual number: {act_num}")
            ui = int(input("Enter you guess: "))
            print(hint(ui, act_num))
            if check_right_guess(ui, act_num):
                user_score += 1
                break
        number_replay += 1
    else :
        print("Thanks for playing")
        break