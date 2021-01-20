from termcolor import colored

"""by MSKF"""


# Help
print(colored("Welcoem to Calculator !\n", "magenta"))
print("Actions:")
print("'+' for addition")
print("'-' for subtraction")
print("'*' for multiplication")
print("'/' for division\n")


# Application
def app():

    # Get the first number
    while True:
        try:
            number = float(input(colored("Enter a number: ", "yellow")))
            break
        
        # If the input undefind
        except ValueError:
            print(colored("** Enter a number **", "red"))
            continue

    
    # Get the action
    while True:
        action = input(colored("Enter the action (Enter 'DONE' to finish): ", "white"))


        # Check the action
        if action.upper() == "DONE":
            print(colored(f"Resault: {number}\n\n", "green"))
            app()

        elif action == "-":
            pass

        elif action == "*":
            pass

        elif action == "/":
            pass

        elif action == "+":
            pass

        else:
            print(colored("** Your action isn't avalable **", "red"))
            continue


        # Get the second number
        while True:
            try:
                number2 = float(input(colored("Enter a number: ", "yellow")))
                break

            # If the input undefind
            except ValueError:
                print(colored("** Enter a number **", "red"))
                continue


        # Do the action
        if action == "+":
            number += number2

        elif action == "-":
            number -= number2

        elif action == "*":
            number *= number2

        elif action == "/":
            if number % number2 != 0:
                q = input(colored("Do you like to round it? [Y]es , [N]o ", "white"))

                if q.lower() == "Y":
                    number /= number2
                    number = float(round(number))

                else:
                    number /= number2

            else:
                number /= number2
            


# Run the app
app()
