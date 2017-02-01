import random

def gen_num():
    return random.randint(1, 100)

def play():
    iter = 'y'
    ran = gen_num()
    count = 0

    while iter == 'y':
        guess = int(input("Enter guess (1-100): "))
        count += 1
        
        if guess > ran:
            print("Too high!")
        elif guess < ran:
            print("Too low!")
        else:
            print("Congratulations!!!\nIt took you", count, "guesses!")
            iter = input("Do you want to play again? (y or n) ")
            count = 0
            ran = gen_num()

    print("Thank you for playing!")
