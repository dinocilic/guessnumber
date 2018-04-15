#!/usr/bin/python3
## Guess the Number ! ##
import random, sys, time
from datetime import datetime

def intro():
    print("\n\tHowdy!\nWelcome to Guessing game!\n")
    name = input("What is your name? ")
    now = datetime.now()

    if name == "" or name.isnumeric():
        print("\nSorry, wrong info!\n")
        return intro()
    else:
        print("\nWelcome " + name.capitalize())
        print("You are using: " + sys.platform.capitalize())
        print("Current time is: %02d/%02d/%04d %d:%d:%d\n" % (now.month, now.day, now.year, now.hour, now.minute, now.second))
        return ready_info()

def ready_info():
    ready = input("Are you ready to play? (Y/n) ")
    if ready in ['Y', 'y', 'yes', 'YES', 'Yes']:
        print("\n\tGoodluck!\n")
        return game_on()
    elif ready in ['N', 'n', 'no', 'NO']:
        not_ready = input("Are you sure? (Y/n) ")
        if not_ready in ['Y', 'y', 'yes', 'YES', 'Yes']:
            print("Okay then, Goodluck and see you again!")
            return False
        elif not_ready in ['N', 'n', 'no', 'NO']:
            print("\n\tLet's play!\n")
            return game_on()
        elif not_ready.isnumeric():
            print("\nSorry, wrong info!\nExiting now....")
            time.sleep(0.1)
    else:
        print("\n\tWrong input!\n")
        return ready_info()

def game_on():
    tries = 6
    secret_num = random.randint(1, 20)
    print("\nSo, I'am thinking on a number between 1 and 20!")
    print("\n\tYou have " + str(tries) + " tries!\n")

    for guess in range(7, 1, -1):
        guess_num = int(input("Take a guess: "))

        if guess_num < secret_num:
            print("You guessed lower!\n")
            guess = guess - 2
            print("\t" + str(guess) + " more to go\n")
            if guess == 0:
                print("\tNo more tries, sorry :(\n")
                return go_again()
        elif guess_num > secret_num:
            print("You guessed higher!\n")
            guess = guess - 2
            print("\t" + str(guess) + " more to go\n")
            if guess == 0:
                print("\tNo more tries, sorry :(\n")
                return go_again()
        elif guess_num == secret_num:
            guess = guess - 2
            print("\n\tBravo you guessed my number! And you had " + str(guess) + " more to go.\n")
            return go_again()

def go_again():
    again = input("Do you want to play another game? (Y/n) ")
    if again in ['Y', 'y', 'yes', 'YES', 'Yes']:
        print("\nOkay, here we go again!\n")
        return game_on()
    elif again in ['N', 'n', 'no', 'NO']:
        print("\n\tThank you for playing, hope to see you again!\n")
        return False
    elif again.isnumeric():
        print("Wrong input! Exiting now...")
        return False

if __name__ == '__main__':
    intro()
