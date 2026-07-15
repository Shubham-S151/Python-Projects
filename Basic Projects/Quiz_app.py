"""
Project Title: Console Based Quiz Application

Project Description:
This is a simple command-line quiz application built using basic Python concepts.
The program asks the user multiple-choice questions and checks whether the
entered answer is correct or not. Each question has four options (A, B, C, D).
The user selects an option, and the program compares it with the correct answer.

Concepts Used:
- Variables
- Dictionaries (for storing questions and answers)
- Functions
- For loops
- If–Else conditions
- User input (input function)

At the end of the quiz, the program displays the total score and percentage.
It also gives feedback based on the user's performance.
"""

"""
question_dict = { question : {
                    choices:(1,2,3,4),
                    answer:1/2/3/4
                            }
                }
"""

# Code Structure 
'''
main while loop
   ├── menu
   ├── admin login
   │      └── admin while loop
   │           ├── add
   │           ├── update
   │           └── remove
   └── student quiz
'''
# question database
question_dict = {
    "1. What is the capital of India?": {
        "choices": ("A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"),
        "answer": 2
    },

    "2. Which language is used for system programming?": {
        "choices": ("A. Python", "B. Java", "C. C++", "D. HTML"),
        "answer": 3
    },

    "3. Who is known as the father of computers?": {
        "choices": ("A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"),
        "answer": 1
    }
}

# login function
def check_login(pas):
    return pas == "1234567"

# helper function for default input
def input_with_default(prompt, default):
    value = input(f"{prompt} [{default}]:")
    if value.strip() == "":
        return default
    return value

# menu
def menu():
    return """Hello, Welcome to Quiz App by Excited Nuclei
Please Select your role:
1. Admin
2. Student
"""

# add question
def add_questions(ques, choices, ans, ques_dict):
    ques_dict[ques] = {
        "choices":choices,
        "answer":ans
    }

# remove question
def remove_questions(ques, ques_dict):
    if ques in ques_dict:
        del ques_dict[ques]
        print("Question removed successfully.")
    else :
        print("Question not found!")

# update question
def update_questions(ques, choices, ans, ques_dict):
    if ques in ques_dict:
        ques_dict[ques]["choices"] = choices
        ques_dict[ques]["answer"] = ans
        print("Question updated successfully.")
    else :
        print("Question not found!")

# quiz start
def quiz_init():
    score = 0
    total = len(question_dict)

    print("\nWelcome to the Quiz!") 
    print("Total Questions:", total)
    print("Enter option number (1-4)\n")

    for ques,data in question_dict.items():
        print("\n", ques)
        for c in data["choices"]:
            print(c)
        user_ans = int(input("Enter your answer (1 - 4): "))
        if user_ans == data['answer']:
            print("Correct!")
            score+=1
        else :
            print("Wrong! Correct answer was option", data["answer"])

    percentage = (score/total)*100

    print("\nQuiz Finished!")
    print("Score:", score, "/", total) # >> Score: 3/3
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good job!")
    else:
        print("Keep practicing!")

# Main Loop
while True:
    print(menu())
    role = int(input("Enter your role: "))

    # Admin Section
    if role == 1:
        pas = input("Please enter your password: ")

        if check_login(pas):
            while True:
                print("\nAdmin Panel")
                print("1. Add Question")
                print("2. Update Question")
                print("3. Remove Question")
                print("4. Back to Main Menu")
                
                ip = int(input("Enter your choice: "))
                # ADD QUESTION
                if ip==1:
                    ques = input("Enter question: ")
                    c1 = input("Enter choice 1: ")
                    c2 = input("Enter choice 2: ")
                    c3 = input("Enter choice 3: ")
                    c4 = input("Enter choice 4: ")

                    ans = int(input("Enter correct answer (1-4): "))
                    choices = (c1, c2, c3, c4)
                    add_questions(ques, choices, ans, question_dict)
                    print("Question added successfully!")
                # UPDATE QUESTION
                elif ip == 2:
                    ques = input("Enter question to update: ")
                    if ques in question_dict:
                        old_choices = question_dict[ques]["choices"]
                        old_answer = question_dict[ques]["answer"]

                        c1 = input_with_default("Choice 1", old_choices[0])
                        c2 = input_with_default("Choice 2", old_choices[1])
                        c3 = input_with_default("Choice 3", old_choices[2])
                        c4 = input_with_default("Choice 4", old_choices[3])
                        ans = input_with_default("Correct answer (1-4)", old_answer)
                        ans = int(ans)

                        choices = (c1, c2, c3, c4)

                        update_questions(ques, choices, ans, question_dict)
                    else :
                        print("Question not found.")
                # REMOVE QUESTION
                elif ip == 3:
                    ques = input("Enter question to remove: ")
                    remove_questions(ques, question_dict)
                # BACK TO MAIN MENU
                elif ip == 4:
                    break                    
                else :
                    print("Invalid Choice!")
    # Student Section
    elif role == 2:
        print("\nStarting Quiz...")
        quiz_init()
    else :
        print("Invalid role")

    # EXIT OPTION
    exit_choice = input("\nDo you want to exit the program? (y/n): ")

    if exit_choice.lower() == "y":
        print("Thank you for using Quiz App!")
        break