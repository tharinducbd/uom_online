# 4.4: Functions

from math import pi

# Function definition: def keyword, function name, parameters
def print_me(msg: str='Hi!') -> None:
    # Docstring and the suit of code
    """Print a capitalized message in terminal"""
    print(msg.upper())
    # The return statement. Not using an expression will return None.
    return

print_me("This is Python")
print_me()
print(print_me.__doc__)

# Exercise 1
def greet(name: str) -> None:
    """Print 'Hello!, name' in terminal"""
    print(f"Hello!, {name}")
    return

greet("Monty Python")

# Exercise 2
def calc_circumference(r):
    return 2 * pi * r

def calc_area(r):
    return pi * r**2

print("{:.3f}".format(calc_circumference(10)))
print("{:.3f}".format(calc_area(r=10)))

# Arbitrary arguments
def log(*args):
    print("-----", end="")
    for entry in args:
        print(entry, end="-----")
    print()
    return

log("Life", "Universe", "and", "Everything")

