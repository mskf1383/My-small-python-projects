"""by MSKF"""


from termcolor import colored
import random, os

# Clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Level
level = 1


# Score
score = 0


# Game
def game(score, level):
    # First clear the screen
    clear_screen()


    # levels
    if score >= level * 100:
        level += 1
        print(colored(f"You reach level {level} !!!", "green"))
        input("Continue > ")
        game(score, level)


    # Welcom message
    print(colored("Wellcome to the game.", "magenta"))
    print(colored(f"** Your are level {level} **", "blue"))
    print(colored(f"** Your score is {score} **\n", "blue"))
    print(colored("Answer the quetion : ", "whtite"))


    # Numbers
    x = random.randint(0, level * 10)
    y = random.randint(0, level * 10)
    z = random.randint(0, level * 10)


    # For select a random phrase
    random_num = random.randint(0, 3)


    # The list of valid quetions
    quetion_list = [
        f"{x} + {y} + {z}",
        f"{x} - {y} - {z}",
        f"{x} - {y} + {z}",
        f"{x} + {y} - {z}"
    ]


    # The list of valid answers
    answer_list = [
        x + y + z,
        x - y - z,
        x - y + z,
        x + y - z
    ]


    # Quetion & Answer variables
    quetion = quetion_list[random_num]
    answer = answer_list[random_num]


    # Print phrase 
    print(quetion)


    # Check the answer
    user_answer = input(" > ")
    if user_answer.upper() == "UPGRADE":
            input(colored("Upgrade > ", "white"))
            score += 1000
            game(score, level)

    try:
        if int(user_answer) == answer:
            print(colored("Excellent ! Your answer is true.", "green"))
            input("Next > ")
            score += 10
            game(score, level)

        if user_answer == "CHEAT":
            print(colored("Excellent ! Your answer is true.", "green"))
            input("Next > ")
            score += 10
            game(score, level)

        else:
            print(colored(f"Oh no! Your answer is false. \nTrue answer is {answer}", "red"))
            input("Next > ")
            score -= 1
            game(score, level)

    except ValueError:
        input(colored("Enter a valid answer.", "red"))
        game(score, level)


# Start the game
game(score, level)