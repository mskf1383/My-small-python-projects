"""by MSKF"""


import random
import os

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
        print("You reach level {}!!!".format(level))
        input("Continue> ")
        game(score, level)


    # Welcom message
    print("Wellcome to the game.")
    print("** Your are level {} **".format(level))
    print("** Your score is {} **".format(score))
    print("Answer the quetion:")


    # Numbers
    x = random.randint(0, level * 10)
    y = random.randint(0, level * 10)
    z = random.randint(0, level * 10)


    # For select a random phrase
    random_num = random.randint(0, 3)


    # The list of valid quetions
    quetion_list = [
        "{} + {} + {}".format(x, y, z),
        "{} - {} - {}".format(x, y, z),
        "{} - {} + {}".format(x, y, z),
        "{} + {} - {}".format(x, y, z),
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
    user_answer = input("> ")
    if user_answer.upper() == "UPGRADE":
            input("Upgrade> ")
            score += 1000
            game(score, level)

    try:
        if int(user_answer) == answer:
            print("Exellent! Your answer is true.")
            input("Next> ")
            score += 10
            game(score, level)

        if user_answer == "CHEAT":
            print("Exellent! Your answer is true.")
            input("Next> ")
            score += 10
            game(score, level)

        else:
            print("Oh no! Your answer is false. \nTrue answer is {}".format(answer))
            input("Next> ")
            score -= 1
            game(score, level)

    except ValueError:
        input("Enter a valid answer.")
        game(score, level)


# Start the game
game(score, level)