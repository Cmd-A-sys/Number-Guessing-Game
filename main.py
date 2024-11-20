import random as r
import time
chances = {12:"Easy",8:"Medium",4:"Hard"}
difficulties = {1:chances[12],2:chances[8],3:chances[4]}
def choose():
    return r.randint(1,100)
def difficulty():
    print("Please choose a difficulty:\n\n1.Easy (12 Chances)\n2.Medium (8 Chances)\n3.Hard (4 Chances)")
    return int(input(""))
def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    try:
        dif = difficulty()
    except ValueError:
        print("Please enter a number 1 through 3")
        dif = difficulty()
    print("Great! You've selected the",difficulties[dif],"difficulty\nLet's start!")
    choice_count = 0
    guess = False
    comp_num = choose()
    if dif == 1:
        choice_count = 12
    elif dif == 2:
        choice_count = 8
    elif dif == 3:
        choice_count = 4
    while choice_count > 0 or guess:
        choice = int(input("Enter a number between 1 and 100:"))
        if choice != comp_num:
            print("Incorrect!",end="")
            if choice>comp_num:
                print("The number is less than",choice,"\n")
            elif choice<comp_num:
                print("The number is greater than",choice,"\n")
        else:
            print("Correct!")
            while input("Do you want to play again? (y/n)\n") == "y":
                game()
            quit()
        choice_count -= 1
    print("You're out of turns! The number is",comp_num)
    while input("Do you want to play again? (y/n)\n") == "y":
        game()
    quit()
game()