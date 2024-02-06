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
    # check all the rows for a win
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "" :
            return True
    # check all the columns for a win
    for column in range(3):
         if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            return True
    # check diagonal win conditions
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    elif empty_spaces() is False:
        return "Tie"
    else:
        return False


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