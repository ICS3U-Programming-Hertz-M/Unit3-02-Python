#!/usr/bin/env python3

# Created by: Hertz Antonella
# Created on: 28 mar 2022
# This program ask the user to guess any number between 0 and 9
import constants


def main():
    # this function ask the user to guess a number
    guess_number = int(input("Guess_any_number from 0 to 9:"))
    print("")

    # compare the number entered to the true number
    if guess_number == 6:
        print("correct guess!")
    else:
        print("your guess is incorrect")


if __name__ == "__main__":
    main()
