"""by MSKF"""


from random import randint as number
import os


# Program
def program():
    input("Enter the web adress to hack: ")
    x = 0

    # Loop
    while True:
        random_number = number(0, 1)
        x += random_number

        if x == 9999999:
            input("| HACKED |")
            break

        else:
            print(random_number, end="")


# Run the program
program()