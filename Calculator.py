"""by MSKF"""


# Help
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
            number = float(input("Enter a number: "))
            break
        
        # If the input undefind
        except ValueError:
            print("** Enter a number **")
            continue

    
    # Get the action
    while True:
        action = input("Enter the action (Enter 'DONE' to finish): ")


        # Check the action
        if action.upper() == "DONE":
            print("Resault: {}".format(number) , end="\n\n")
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
            print("** Your action isn't avalable **")
            continue


        # Get the second number
        while True:
            try:
                number2 = float(input("Enter a number: "))
                break

            # If the input undefind
            except ValueError:
                print("** Enter a number **")
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
                q = input("Do you like to round it? [yes/no] ")

                if q.lower() == "yes":
                    number /= number2
                    number = flout(round(number))

                else:
                    number /= number2

            else:
                number /= number2
            


# Run the app
app()