# Arithmetic functions
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


# Helper functions for select_op
def validate_op(operation):
    accepted_ops = ["+", "-", "*", "/", "^", "%", "#", "$"]
    if operation not in accepted_ops:
        return False
    return True


def is_input_op(user_input):
    if '#' or '$' in user_input:
        return True
    else:
        return False


def is_input_num(user_input):
    try:
        num = float(user_input)
    except ValueError:
        return False
    else:
        return True


def select_op(operation):
    if not validate_op(operation):
        print("Unrecognized operation")
        return None

    if operation == "#":
        return -1
    elif operation == "$":
        return None

    a = input("Enter first number: ")
    print(a)
    re_prompt_input = True
    while re_prompt_input:

        if is_input_op(a):
            if a == '#':
                return -1
            elif a[-1] == '$':
                return None

        if not is_input_num(a):
            a = input("Enter first number: ")
            print(a)
            continue

        re_prompt_input = False

    b = input("Enter second number: ")
    print(b)
    re_prompt_input = True
    while re_prompt_input:

        if is_input_op(b):
            if b == '#':
                return -1
            elif b[-1] == '$':
                return None

        if not is_input_num(b):
            b = input("Enter first number: ")
            print(b)
            continue

        re_prompt_input = False

    a, b = float(a), float(b)
    if operation == "+":
        print(a, "+", b, "=", add(a, b))
    elif operation == "-":
        print(a, "-", b, "=", subtract(a, b))
    elif operation == "*":
        print(a, "*", b, "=", multiply(a, b))
    elif operation == "/":
        if b == 0:
            print("float division by zero")
            print(a, "/", b, "=", "None")
            return
        print(a, "/", b, "=", divide(a, b))
    elif operation == "^":
        print(a, "^", b, "=", power(a, b))
    elif operation == "%":
        print(a, "%", b, "=", remainder(a, b))

    return None


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
