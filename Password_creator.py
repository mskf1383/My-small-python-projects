"""by MSKF"""

from random import choice
from termcolor import colored
from hashlib import md5

# List of avalable words, numbers, symbols
words_list = [
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L',
    'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w',
    'X', 'x', 'Y', 'y', 'Z', 'z'
]
numbers_list = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]
symbols_list = [
    '!', '@', '#', '$', '%', '^', '&', '*', '[', ']', '{', '}', '_', "|", "(", ")", "="
]

characters_list = words_list + numbers_list + symbols_list


def program():
    # Get the lenght of password
    try:
        lenght = int(input(colored("Enter the lenght of password: ", "yellow")))

    except ValueError:
        input(colored("** Enter a number!!! **\n", "red"))
        program()

    # The default password
    password = ''

    # Create the password
    while lenght:
        password += choice(characters_list)
        lenght -= 1

    password = md5(password.encode("UTF-8")).hexdigest()

    # Print the password
    print(password)

    # Exit the program
    input("Exit > ")


# Start the program
program()
