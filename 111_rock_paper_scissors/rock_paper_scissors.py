import random

options = ("Rock", "Paper", "Scissors", "Exit")
user_input = ""

while user_input != "Exit":
    print("Choose option -- Rock, Paper, Scissors, Exit:")
    opponent = random.choice(("Rock", "Paper", "Scissors"))
    user_input = input("Enter option: ")

    while user_input not in options:
        user_input = input("Enter option: ")
        if user_input not in options:
            print("Enter proper option!")

    print("Computer:", opponent)
    print("Player:", user_input)

    if opponent == user_input:
        print("Round draw")
    if ((opponent == "Rock") and (user_input == "Scissors")):
        print("Computer wins!")
    if ((opponent == "Scissors") and (user_input == "Paper")):
        print("Computer wins!")
    if ((opponent == "Paper") and (user_input == "Rock")):
        print("Computer wins!")    
    if ((opponent == "Scissors") and (user_input == "Rock")):
        print("Player wins!")
    if ((opponent == "Paper") and (user_input == "Scissors")):
        print("Player wins!")
    if ((opponent == "Rock") and (user_input == "Paper")):
        print("Player wins!")    
    