from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Rock, Paper & Scissors")


head_label = Label(text="ROCK - PAPER - SCISSORS")
head_label.grid(column=0, row=0, columnspan= 3)

rock_img = PhotoImage(file="images/rock.png")
scissors_img = PhotoImage(file="images/scissors.png")
paper_img = PhotoImage(file="images/paper.png")


btn_rock = Button(root, image=rock_img, bg='#eeeeee', border=0, command= lambda: Click("Rock"))
btn_rock.grid(row = 1, column=0)


btn_paper = Button(image=paper_img, bg='#eeeeee', border=0, command= lambda: Click("Paper")) 
btn_paper.grid(row = 1, column=1)


btn_scissors = Button(image=scissors_img, bg='#eeeeee', border=0, command= lambda: Click("Scissors")) 
btn_scissors.grid(row = 1, column=2)      


player_choise_label = Label(text="Player choise: ", fg='green')
player_choise_label.grid(column=0, row=3, columnspan= 3)


computer_choise_label = Label(text="Computer choise: ", fg='red')
computer_choise_label.grid(column=0, row=4, columnspan= 3)


result_label = Label(text="result")
result_label.grid(column=0, row=5, columnspan= 3)


player_wins_label = Label(text="Player: ")
player_wins_label.grid(column=0, row=6, columnspan= 3)


computer_wins_label = Label(text="Computer: ")
computer_wins_label.grid(column=0, row=7, columnspan= 3)


player_wins = 0
computer_wins = 0


def Click(btn_name):
    player_choise_label["text"] = btn_name
    options = ("Rock", "Paper", "Scissors")
    computer_choise_label["text"] = random.choice(options)
    global computer_wins
    global player_wins


    if computer_choise_label["text"] == player_choise_label["text"]:
        result_label["text"] = "Round draw"
        result_label["fg"] = "grey"

    if (computer_choise_label["text"] == "Rock") and (player_choise_label["text"] == "Scissors"):
        result_label["text"] = "Computer wins!"
        result_label["fg"] = "red"
        computer_wins += 1

    if ((computer_choise_label["text"] == "Scissors") and (player_choise_label["text"] == "Paper")):
        result_label["text"] = "Computer wins!"
        result_label["fg"] = "red"
        computer_wins += 1

    if ((computer_choise_label["text"] == "Paper") and (player_choise_label["text"] == "Rock")):
        result_label["text"] = "Computer wins!"
        result_label["fg"] = "red"
        computer_wins += 1

    if ((computer_choise_label["text"] == "Scissors") and (player_choise_label["text"] == "Rock")):
        result_label["text"] = "Player wins!"
        result_label["fg"] = "green"
        player_wins += 1

    if ((computer_choise_label["text"] == "Paper") and (player_choise_label["text"] == "Scissors")):
        result_label["text"] = "Player wins!"
        result_label["fg"] = "green"
        player_wins += 1

    if ((computer_choise_label["text"] == "Rock") and (player_choise_label["text"] == "Paper")):
        result_label["text"] = "Player wins!"
        result_label["fg"] = "green"
        player_wins += 1
    
    player_wins_label["text"] = str(player_wins)
    computer_wins_label["text"] = str(computer_wins)


root.mainloop()