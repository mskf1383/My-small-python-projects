"""by MSKF"""

from termcolor import colored

# The list
shopping_list = []


# Helps
def show_help():
    print("You can add items.")
    print("Enter \'DONE\' to finish adding.")
    print("Enter \'HELP\' to show help.")
    print("Enter \'SHOW\' to see your list.")
    print("Enter \'REMOVE\' to remove an item.")


# Show the list
def show_list():
    print("Here\'s your list: ")
    num = 1

    for item in shopping_list:
        print(f"{num}. {item}")
        num += 1


# Add an item to the list
def add_to_list(x):

    if shopping_list.count(x.lower()) != 0:
        print(colored(f"{x} added before.", "red"))

    else:
        shopping_list.append(x.lower())
        num = len(shopping_list)
        print(colored(f"{x} added to list.\n Your list has {num} items now.", "green"))


# Remove an item to the list
def remove_from_list(z):
    z = input("What do you want to remove? ")

    if list(z) <= shopping_list:
        shopping_list.remove(z)
        num = len(shopping_list)
        print(f"{z} removed from list.\n Your list has {num} items now.")

    else:
        print(f"{z} isn\'t in your list!!!")


# Program
def run_app():

    # Show the help
    show_help()


    # Check the answer
    while True:
        x = input("> ")


        # If done
        if x.upper() == "DONE":
            show_list()
            break

        # If help
        elif x.upper() == "HELP":
            show_help()
            continue

        # If show
        elif x.upper() == "SHOW":
            show_list()
            continue

        # If remove
        elif x.upper() == "REMOVE":
            remove_from_list(x)
            continue

        # Else
        else:
            add_to_list(x)


# Start the program
run_app()