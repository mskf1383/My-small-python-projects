"""by MSKF"""


def game():
    import random

    # Select a random number
    secret_num = random.randint(1, 10)

    while True:

        # Get a number from player
        try:
            guess = int(input("Enter a number between 1 & 10: "))

        except ValueError:
            print("Pleas enter a number")


        # Check the number
        if guess == secret_num:
            print("You win!!! My number is {}." .format(secret_num))
            break

        elif guess < secret_num:
            print("No!!! Come UP")
            continue

        elif guess > secret_num:
            print("No!!! Come DOWN")
            continue

        else:
            print("No!!! Try again.")
            continue


    # Play again
    play_again = input("Do you want to play again? Entar \'YES\' to play again: ")

    if play_again.upper() == "YES":
        game()


# Run the game
game()