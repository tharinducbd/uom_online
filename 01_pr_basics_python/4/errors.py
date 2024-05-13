# Errors

# NameError: when accessing an undefined variable
# try:
#     print(num)
# except NameError:
#     print("NameError encountered")

# IndexError: when an out of range index value is referenced
my_list = list(range(5))
try:
    print(my_list[10])
except IndexError:
    print("IndexError encountered")

# TypeError: when an operation/ function is applied to an incorrect type
try:
    'colin' + 1
except TypeError:
    print("TypeError encountered")

# ValueError: when a built-in operation or function receives an
# argument that has the righy type but an invalid value
try:
    x = int("hello")
    print(x)
except ValueError:
    print("ValueError encountered")

# ImportError: when something is wrong with an import statment
# try:
#     import dummy_module
# except ImportError:
#     print("ImportError encountered")

# Example
try:
    num_val = int("Num")
except:
    num_val = -1

if num_val > 0:
    print("num_val is a number")
else:
    print("num_val ain't no number...")
