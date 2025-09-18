# Generates headings (eg: ---- Heading ----)
from C_02_factors_int_checker import to_factor


def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
To use this program, simply enter an integer between 
1 and 200 (inclusive). The program will show the factors of 
your chosen integer.

It will also tell you if your chosen number ...
- is unity (1) as it only has one factor
- is a prime number (i.e. it has two factors)
- is a perfect square

To exit the program, please type 'xxx'
    ''')


# Ask user for an integer between 1 and 200.
def num_check(question):

    error = "Please enter a number between 1 and 200\n"
    while True:

        try:
            #ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Works out factors, returns sorted list
def factor(var_to_factor):
    factors_list = []

    # square root the number to work out when to stop looping.
    stop =
    stop = int(stop)

    for item in

        # check to see if the item is a factor
        if to_factor

            # Calculate partner
            partner =

            # Add partner to the list (but prevent duplicate entries)
            if partner ==

    # return the sorted list
    factors_list.sort()
    return factors_list

# Main Routine Goes Here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

    while True:

        comment = ""

        # ask user for number to be factorised
        to_factor = num_check("\nEnter an integer (or xxx to quit: ")

        if to_factor == "xxx":
            break

        # get factors for integers that are 2 or more
        elif to_factor != 1:
            all_factors = factor(to_factor)

        # Set up comment for unity
        else:
            all_factors = ""
            comment = "One is UNITY! It only has one factor. Itself :)"

        # comments for squares / primes

        # Prime numbers have only two factors
        if len(all_factors) == 2:
            comment = f"{to_factor} is a prime number"

        # check if the list has an odd number of factors
        elif len(all_factors) % 2 == 1:
            comment = f"Factors of {to_factor} is a perfect square"

        # Set up headings
        if to_factor > 1:
            heading = "One is special..."

        # output factors and comment
        print()
        statement_generator(heading, "*")
        print(all_factors)
        print(comment)

    print("Thank you for using the factors calculator")