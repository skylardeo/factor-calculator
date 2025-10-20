# Generates headings (eg: ---- Heading ----)
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

        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            #ask the user for a number
            response = int(response)

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
    # to_factor = num_check("To factor: ")

    # square root the number to work out when to stop looping.
    stop = var_to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop + 1):

        # check to see if the item is a factor
        if to_factor % item == 0:
            factors_list.append(item)

            # calculate partner
            partner = to_factor // item

            # add partner to the list (but prevent duplicates)
            if partner not in factors_list:
                factors_list.append(partner)

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
    to_factor = num_check("\nTo factor? (or xxx to quit: ")

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
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # output factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

    print("Thank you for using the factors calculator")