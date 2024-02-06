from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        buttons[row][column]["text"] = player
        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=player + " turn")
        elif check_winner() is True:
            label.config(fg="#6cc4a0")
            label.config(text=player + " wins")
        elif check_winner() == "Tie":
            label.config(text="Tie")
        else:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=player[0] + " turn")
            elif check_winner() is True:
                label.config(fg="#6cc4a0")
                label.config(text=players[1] + "wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")

def check_winner():
    # check all the rows for a win
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "" :
            buttons[row][0].config(fg="#6cc4a0")
            buttons[row][1].config(fg="#6cc4a0")
            buttons[row][2].config(fg="#6cc4a0")
            return True
    # check all the columns for a win
    for column in range(3):
         if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(fg="#6cc4a0")
            buttons[1][column].config(fg="#6cc4a0")
            buttons[2][column].config(fg="#6cc4a0")
            return True
    # check diagonal win conditions
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(fg="#6cc4a0")
        buttons[1][1].config(fg="#6cc4a0")
        buttons[2][2].config(fg="#6cc4a0")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(fg="#6cc4a0")
        buttons[1][1].config(fg="#6cc4a0")
        buttons[2][0].config(fg="#6cc4a0")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                label.config(fg="#d6d44b")
                buttons[row][column].config(fg="#d6d44b")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"]  != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

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