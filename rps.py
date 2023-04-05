import random

""" create a program where you can play rock, paper, or scissors against the computer.
"""

def play():
    user = input('Rock, Paper, or Scissors?: ')
    
    usr = user[:1].strip().casefold()

    computer = random.choice(["r", "p", "s"]) 

    def cmove(c): 
        if c == "r":
            return "Rock"
        if c == "s":
            return "Scissors"
        if c == "p":
            return "Paper"

    for i in computer:
        result = cmove(i)
        print('Opponent\'s Move: ', result)
   
    if is_win(usr, computer):
        return "Player wins!"

    if is_win(computer,usr):
        return "You lose!"

    if usr == computer:
        return "Draw!"

def is_win(player, opponent):
    #return true
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())
#make it more complicated to allow R, Rock, r, rock etc. as acceptable answers.



