# Files

# Opening and closing a file
file_handle = open("lorem_ipsum_1.txt", "r") # 'r' is optional as it is the default
file_handle.close()

# Reading from a file: read()   >> read entire file as a string
file_handle = open("lorem_ipsum_1.txt", "r")
file_contents = file_handle.read()
file_handle.close()
# print(file_contents)

# Reading from a file: readline()    >> read one line at a time.
file_handle = open("lorem_ipsum_1.txt", "r")
file_contents = file_handle.readline()
print(file_contents)
file_contents = file_handle.readline()
print(file_contents)
file_handle.close()

# Reading from a file: readlines()   >> return a list of lines
file_handle = open("lorem_ipsum_1.txt", "r")
file_contents = file_handle.readlines()
for line in file_contents:
    print(line)
file_handle.close()

# Writing to a file: write(string)
file_handle = open("lorem_ipsum_2", "w")
my_string = "Python is excellent.\nAnd File handline is so easy.\nAnd everything else!"
file_handle.write(my_string)
file_handle.close()

# Appending to a file: append()
file_handle = open("lorem_ipsum_2", "a")
my_string = "\nThe appended line.\nAnother appended line."
file_handle.write(my_string)
file_handle.close()

with open("lorem_ipsum_1.txt", "r") as fh:
    print(fh.readline())
