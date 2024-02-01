from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"]  == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=player[1] + " turn")
            elif check_winner() is True:
                label.config(text=players[0] + "wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=player[0] + " turn")
            elif check_winner() is True:
                label.config(text=players[1] + "wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")




def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]

player = random.choice(players)
buttons = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

label = Label(text=player + " turn", font=("Comic Sans MS",  40), pady=10)
label.pack(side="top")

frame = Frame(window, padx=10)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Comic Sans MS",  40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

reset_button = Button(window, text="Reset", font=("Comic Sans MS",  20), command=new_game)
reset_button.pack(side="bottom")


window.mainloop()