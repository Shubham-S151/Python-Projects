# Project: Rock Paper Scissors Game
# This is a beginner level project that allows to play most common game rock paper scissor
# This program is going to be using additional library "Random"

import random

# Constants
SCORE = 0 # every time user wins going to add 1 to it
REPLAYS = 0 # how many times user choose to play

# Rules: 
# Rock     beats Scissors
# Scissors beats Paper
# Paper    beats Rock
choices = ['Rock', "Paper", "Scissors"]
map_choices = {'Rock':0, "Paper":1, "Scissors":2}
user_map = {0:'Rock', 1:"Paper", 2:"Scissors"}

# genrate the random choice between rock, paper and scissors
def comp_choice(choices:list) -> str:
    """This function will return us the ranndom choice from computer."""
    return random.choice(choices)

# for i in range(11):
#     print(comp_choice(choices))

# check winner
def check(comp_choice:str, user_choice:str, map_choices:dict = map_choices) -> str:
    """This function is going to check who is winner and returns us \
        \n'u' -> if user wins\
        \n'c' -> if computer wins\
        \n'd' -> if there is draw"""
    user_choice = map_choices.get(user_choice)
    comp_choice = map_choices.get(comp_choice)
    if user_choice == comp_choice:
        return 'd'
    # situations in which user wins = [[(0,2),(2,1),(1,0)]]
    elif ((user_choice == 0 and comp_choice == 2) or
          (user_choice == 2 and comp_choice == 1) or 
          (user_choice == 1 and comp_choice == 0)):
        return 'u'
    else :
        return 'c'

m = """\nWelcome to Rock-Paper-Scissors Game by Excited Nuclei.\
    \nPlease select the following for your choice:\
    \nChoice     |   Press\
    \n-----------|--------\
    \nRock       |       0\
    \nPaper      |       1\
    \nScissors   |       2\
    \nExit       |       4"""

win_probability = None
while True:
    comp = comp_choice(choices)
    print(m)
    user = int(input("Enter Your Choice: "))
    if user is not None:
        if user in [0,1,2]:
            if win_probability is None:
                win_probability = "N/A"
            else :
                win_probability = round(SCORE/REPLAYS, 4)*100
            print(f"Your Score: {SCORE} | Replays: {REPLAYS} | Your Win Probability: {win_probability}%")        
            print(f"Your Choice: {user_map.get(user)} | Computer choice: {comp}")
            if check(comp,user_map.get(user)) == "u":
                print("You Win!")
                SCORE+=1
            elif check(comp,user_map.get(user)) == 'd':
                print("There is a Draw")
            else :
                print("You Fail!")
            REPLAYS+=1
        elif user == 4 :
            print(f"Your Score: {SCORE} | Replays: {REPLAYS} | Your Win Probability: {win_probability}%")
            print("Thanks for playing with us!")
            break
        else :
            print(f"Invalid Input: {user}")
    else :
        print("Please give input to game.")