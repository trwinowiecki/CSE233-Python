import random

def gen():
    ran = random.randint(1, 3)
    if ran == 1:
        return "rock"
    elif ran == 2:
        return "paper"
    else:
        return "scissors"

def lose():
    print("You lost!")

def win():
    print("You win!!!")

def draw():
    print("DRAW!")

def play():
    end = False

    while not end:
        ai = gen()
        player = input("Choose 'rock', 'paper' or 'scissors': ")

        if player == 'rock':
            if ai == 'rock':
                draw()
            elif ai == 'paper':
                lose()
                end = True
            else:
                win()
                end = True
        elif player == 'paper':
            if ai == 'paper':
                draw()
            elif ai == 'scissors':
                lose()
                end = True
            else:
                win()
                end = True
        else:
            if ai == 'scissors':
                draw()
            elif ai == 'rock':
                lose()
                end = True
            else:
                win()
                end = True
