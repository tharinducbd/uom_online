
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a - b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b


def get_input(message):
    user_input = input(message)

    # If a mistake is made, user can enter '$' at the end of input string
    if "$" in user_input:
        return "reset_requested"
    
    if "#" in user_input:
        return "termination_requested"

    # Verify input is a number. If not, prompt re-entering.
    try:
        number = float(user_input)
    except ValueError:
        print("Not a valid number,please enter again")
        return "user_input_failed"
    else:
        return number


def validate_input(user_input):
    if user_input == "reset_requested":
        print("Something went wrong")
        return "reset"
    elif user_input == "termination_requested":
        return "terminate"
    else:
        return user_input


def select_op(choice):
    # Ensure that the requested operation is valie
    accepted_operations = ["+", "-", "*", "/", "^", "%", "#", "$"]
    if choice not in accepted_operations:
        print("Unrecognized operation")
        return

    if choice == "#":
        return -1

    if choice == "$":
        return

    # Get the inputs and check if a reset is requested
    a = get_input("Enter first number:")
    if a != validate_input(a):
        if validate_input(a) == 'reset':
            return
        elif validate_input(a) == 'terminate':
            return -1

    b = get_input("Enter second number:")
    if b != validate_input(b):
        if validate_input(b) == 'reset':
            return
        elif validate_input(b) == 'terminate':
            return -1


    if choice == "+":
        print(a, "+", b, "=", add(a, b))
    elif choice == "-":
        print(a, "-", b, "=", subtract(a, b))
    elif choice == "*":
        print(a, "*", b, "=", multiply(a, b))
    elif choice == "/":
        if b == 0:
            print("float division by zero")
            print(a, "/", b, "=", "None")
            return
        print(a, "/", b, "=", divide(a, b))
    elif choice == "^":
        print(a, "^", b, "=", power(a, b))
    elif choice == "%":
        print(a, "%", b, "=", remainder(a, b))

    return


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")


    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if(select_op(choice) == -1):
        #program ends here
        print("Done. Terminating")
        exit()
