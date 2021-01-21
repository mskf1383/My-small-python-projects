"""by MSKF"""


from termcolor import colored


def game():
    import random

    # Select a random number
    secret_num = random.randint(1, 10)

    while True:

        # Get a number from player
        try:
            guess = int(input("Enter a number between 1 & 10: "))

        except ValueError:
            print(colored("Pleas enter a number", "red"))


        # Check the number
        if guess == secret_num:
            print(f"You win!!! My number is {secret_num}.")
            break

        elif guess < secret_num:
            print(colored("No!!! Come UP", "red"))
            continue

        elif guess > secret_num:
            print(colored("No!!! Come DOWN", "red"))
            continue

        else:
            print(colored("No!!! Try again.", "red"))
            continue


    # Play again
    play_again = input("Do you want to play again? Entar \'YES\' to play again: ")

    if play_again.upper() == "YES":
        game()


# Run the game
game()