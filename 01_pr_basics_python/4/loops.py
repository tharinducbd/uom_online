# 4.2: Loops and Iterations
for counter in [1, 2, 3, 4, 5]:
    print("This is a loop: counter = ", counter)

# range()
print(list(range(10)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))

sum = 0
for i in range(0, 101, 2):
    sum += i
print("Total of even numbers: ", sum)

num, x = 100, []
while num > 0:
    x.append(num)
    num -= 15
print(x)

# Nested loops
for x in range(5):
    for y in range(5):
        print("$", end=" ")
    print()

# for-else example
for letter in ['H', 'E', 'L', 'L', 'O']:
    print(letter, end=" ")
else:
    print(", world!")

for letter in ['H', 'E', 'L', 'L', 'O']:
    print(letter, end=" ")
    if letter == 'O':
        break
else:
    print(" !")
print()

# Prime number finder
i = int(input())
j = 2 # fix the code (1) 
while (j <= (i/j)):
    if not(i%j): 
        print("not a prime")
        break # fix the code (2)
    j = j + 1 # fix the code (3)
if (j > i/j): 
    print ("prime")
