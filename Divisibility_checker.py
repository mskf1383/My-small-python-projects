"""by MSKF"""


# Program
while True:

    # Get the number    
    number = int(input("Enter your number: "))
    divisibility = False


    # Check the divisibility
    for i in range(2, number):

        # If divisible
        if number % i == 0:

            print("{} is divisible to {}.".format(number, i))
            divisibility = True


        # If not divisible
        else:

            continue


    # Last answer if not divisible
    if divisibility == False:

        print("{} isn't divisible.".format(number), end="\n\n")


    # End of divisible numbers
    else:

        print("[END]", end="\n\n")
