"""by MSKF"""

from termcolor import colored
import random, os

# Draw grid
CELLS = [
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0)
]


# Clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Select random locations
def get_locations():
    return random.sample(CELLS, 3)


# Moving the player
def move_player(player, move):
    x, y = player

    if move == "RIGHT":
        x += 1

    if move == "LEFT":
        x -= 1

    if move == "DOWN":
        y -= 1

    if move == "UP":
        y += 1

    return x, y


# Check for valid moves
def get_move(player):
    moves = ["RIGHT", "LEFT", "UP", "DOWN"]
    x, y = player

    if x == 0:
        moves.remove("LEFT")  # Can't move left

    if x == 4:
        moves.remove("RIGHT")  # Can't move right

    if y == 0:
        moves.remove("DOWN")  # Can't move down

    if y == 4:
        moves.remove("UP")  # Can't move up

    return moves


# Draw a map
def draw_map(player, name):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell

        if x < 4:
            line_end = ""

            if cell == player:
                output = tile.format(f"{name}")

            else:
                output = tile.format("_")

        else:
            line_end = "\n"

            if cell == player:
                output = tile.format(f"{name}|")

            else:
                output = tile.format("_|")

        print(output, end=line_end)


# Game
def game_loop(name):
    # Use random locations for player, door, monster
    monster, player, door = get_locations()
    playing = True

    # Game loop
    while playing:
        clear_screen()
        draw_map(player, name)
        valid_moves = get_move(player)
        valid_moves_2 = ["RIGHT", "LEFT", "UP", "DOWN"]

        print(f"You are in room {player}")
        print(f"you can move {', '.join(valid_moves)}")
        print(colored("Enter 'QUIT' to quit", "yellow"))

        # Get the moves
        move = input("> ")
        move = move.upper()

        # Exit the game
        if move == "QUIT":
            break

        if move in valid_moves and valid_moves_2:
            player = move_player(player, move)

            # When the player location = monster location
            if player == monster:
                print(colored("\n ** Oh no! The monster kill you! ** \n", "red"))
                playing = False

            # When the player location = door location
            if player == door:
                print(colored("\n ** Great! You escaped! ** \n", "green"))
                playing = False


            # else
            else:
                pass


        # if player enter an invalid move
        elif move not in valid_moves_2:
            input(colored("\n ** Enter valid move! ** \n", "red"))


        # if player want to move into Walls
        else:
            input(colored("\n ** The walls are hard! Dont run into them! ** \n", "magenta"))


    # Playing again
    else:
        if input("Playing again? [Y/n] ").lower() != "n":
            game_loop(name)


# Wellcome
clear_screen()
print(colored("Welcome to dungeon game!", "magenta"))

# Get the name of player
name = input("Enter your name to start: ")
name = name[0]
clear_screen()

# Start the game
game_loop(name)
